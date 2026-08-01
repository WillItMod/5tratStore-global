#!/usr/bin/env python3
"""Fail-closed validation for 5tratStore GLOBAL app submissions."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - CI installs the dependency
    raise SystemExit("PyYAML is required: python3 -m pip install pyyaml") from exc


ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", ".github", "scripts", "templates"}
REQUIRED_FILES = {
    "5tratstore-app.yml",
    "docker-compose.yml",
    "5tratstore-review.yml",
    "LICENSES.md",
}
MAX_APP_FILE_BYTES = 2 * 1024 * 1024
ALLOWED_APP_SUFFIXES = {
    ".conf",
    ".ini",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".md",
    ".png",
    ".sh",
    ".svg",
    ".txt",
    ".webp",
    ".yaml",
    ".yml",
}
ALLOWED_APP_BASENAMES = {".gitkeep"}
FORBIDDEN_PAYLOAD_SUFFIXES = {
    ".apk",
    ".bin",
    ".deb",
    ".dmg",
    ".exe",
    ".gz",
    ".img",
    ".ipa",
    ".iso",
    ".jar",
    ".msi",
    ".ova",
    ".qcow2",
    ".tar",
    ".tgz",
    ".wasm",
    ".whl",
    ".zip",
}
RIGHTS = {
    "packageOriginal",
    "softwareDistributionCleared",
    "containerUseCleared",
    "listingTextCleared",
    "artworkCleared",
    "noticesIncluded",
}
TESTS = {"installTested", "startTested", "updateTested", "uninstallTested"}
PENDING_TEST_DECLARATIONS = TESTS | {"backupTested", "restoreTested"}
FORBIDDEN_ASSOCIATIONS = re.compile(r"umbrel", re.IGNORECASE)
PINNED_IMAGE_DIGEST = re.compile(r"^.+@sha256:[0-9a-f]{64}$", re.IGNORECASE)
PINNED_GITHUB_BUILD = re.compile(
    r"^https://github\.com/[^/\s]+/[^#\s]+(?:\.git)?#[0-9a-f]{40}$",
    re.IGNORECASE,
)


def load_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict):
        raise ValueError("must contain a YAML object")
    return value


def validate_app(app_dir: Path, allow_pending: bool = False) -> list[str]:
    errors: list[str] = []
    missing = sorted(name for name in REQUIRED_FILES if not (app_dir / name).is_file())
    if missing:
        return [f"{app_dir.name}: missing {', '.join(missing)}"]

    try:
        manifest = load_yaml(app_dir / "5tratstore-app.yml")
        review = load_yaml(app_dir / "5tratstore-review.yml")
        compose = load_yaml(app_dir / "docker-compose.yml")
    except Exception as exc:
        return [f"{app_dir.name}: {exc}"]

    app_id = str(manifest.get("id") or "").strip().lower()
    version = str(manifest.get("version") or "").strip()
    if app_id != app_dir.name.lower():
        errors.append(f"{app_dir.name}: manifest id must match directory name")
    if not version:
        errors.append(f"{app_dir.name}: manifest version is required")
    icon = str(manifest.get("icon") or "").strip()
    local_icon = any((app_dir / name).is_file() for name in ("icon.png", "icon.jpg", "icon.jpeg", "icon.svg", "logo.png", "logo.jpg", "logo.jpeg", "logo.svg"))
    if not local_icon and not icon.startswith("https://"):
        errors.append(f"{app_dir.name}: a local icon or HTTPS upstream icon URL is required")
    review_status = review.get("status")
    review_schema = review.get("schemaVersion")
    if review_schema not in {1, 2}:
        errors.append(f"{app_dir.name}: review must use schemaVersion 1 or 2")
    if review_status != "approved" and not (allow_pending and review_status == "pending"):
        errors.append(f"{app_dir.name}: review must be approved")
    if str(review.get("appId") or "").strip().lower() != app_id:
        errors.append(f"{app_dir.name}: review appId does not match manifest")
    if str(review.get("appVersion") or "").strip() != version:
        errors.append(f"{app_dir.name}: review version does not match manifest")
    for field in ("reviewedAt", "reviewedBy"):
        if not str(review.get(field) or "").strip():
            errors.append(f"{app_dir.name}: review {field} is required")

    upstream = review.get("upstream") if isinstance(review.get("upstream"), dict) else {}
    for field in ("sourceUrl", "license", "licenseEvidence"):
        value = str(upstream.get(field) or "").strip()
        if not value or (field.endswith("Url") or field == "licenseEvidence") and not value.startswith("https://"):
            errors.append(f"{app_dir.name}: upstream {field} must be an HTTPS value")

    rights = review.get("rights") if isinstance(review.get("rights"), dict) else {}
    for field in sorted(RIGHTS):
        if rights.get(field) is not True:
            errors.append(f"{app_dir.name}: rights.{field} must be true")

    delivery = review.get("delivery") if isinstance(review.get("delivery"), dict) else {}
    if delivery.get("mode") != "direct-upstream-artifact":
        errors.append(f"{app_dir.name}: delivery.mode must be direct-upstream-artifact")
    if delivery.get("storePayload") != "recipe-only":
        errors.append(f"{app_dir.name}: delivery.storePayload must be recipe-only")
    if delivery.get("mirrorsThirdPartyPayload") is not False:
        errors.append(f"{app_dir.name}: delivery.mirrorsThirdPartyPayload must be false")

    compatibility = review.get("compatibility") if isinstance(review.get("compatibility"), dict) else {}
    if not compatibility.get("osVersions") or not compatibility.get("architectures"):
        errors.append(f"{app_dir.name}: tested OS versions and architectures are required")
    for field in sorted(PENDING_TEST_DECLARATIONS):
        if review_status == "approved" and compatibility.get(field) is not True:
            if field in TESTS:
                errors.append(f"{app_dir.name}: compatibility.{field} must be true")
        if review_status == "pending" and field not in compatibility:
            errors.append(f"{app_dir.name}: pending review must declare compatibility.{field}")
    if review_schema == 2 and review_status == "approved":
        recovery_tested = (
            compatibility.get("backupTested") is True
            and compatibility.get("restoreTested") is True
        )
        recovery_not_applicable = (
            compatibility.get("backupNotApplicable") is True
            and compatibility.get("restoreNotApplicable") is True
        )
        if not recovery_tested and not recovery_not_applicable:
            errors.append(
                f"{app_dir.name}: schemaVersion 2 approval requires tested backup/restore "
                "or an explicit not-applicable declaration"
            )

    services = compose.get("services") if isinstance(compose.get("services"), dict) else {}
    if not services:
        errors.append(f"{app_dir.name}: compose services are required")
    for service_name, service in services.items():
        if not isinstance(service, dict):
            continue
        image = str(service.get("image") or "").strip()
        if image and (image.endswith(":latest") or ":" not in image.rsplit("/", 1)[-1] and "@sha256:" not in image):
            errors.append(f"{app_dir.name}: service {service_name} image must use a pinned tag or digest")
        if "@sha256:" in image and not PINNED_IMAGE_DIGEST.fullmatch(image):
            errors.append(
                f"{app_dir.name}: service {service_name} image digest must be a 64-character SHA-256"
            )
        build = service.get("build")
        if build:
            if image:
                errors.append(
                    f"{app_dir.name}: service {service_name} source build must not name a store image"
                )
            if isinstance(build, str):
                build_context = build.strip()
                dockerfile = "Dockerfile"
            elif isinstance(build, dict):
                build_context = str(build.get("context") or "").strip()
                dockerfile = str(build.get("dockerfile") or "Dockerfile").strip()
                unexpected = sorted(set(build) - {"context", "dockerfile"})
                if unexpected:
                    errors.append(
                        f"{app_dir.name}: service {service_name} source build has unsupported keys "
                        f"({', '.join(unexpected)})"
                    )
            else:
                build_context = ""
                dockerfile = ""
            if not PINNED_GITHUB_BUILD.fullmatch(build_context):
                errors.append(
                    f"{app_dir.name}: service {service_name} build must use an HTTPS GitHub context "
                    "pinned to a full commit"
                )
            context_source = build_context.rsplit("#", 1)[0].removesuffix(".git").rstrip("/")
            review_source = str(upstream.get("sourceUrl") or "").removesuffix(".git").rstrip("/")
            if context_source.lower() != review_source.lower():
                errors.append(
                    f"{app_dir.name}: service {service_name} build context must match upstream sourceUrl"
                )
            if dockerfile != "Dockerfile":
                errors.append(
                    f"{app_dir.name}: service {service_name} must use the upstream root Dockerfile"
                )
            source_commit = str(upstream.get("sourceCommit") or "").strip().lower()
            context_commit = build_context.rsplit("#", 1)[-1].lower() if "#" in build_context else ""
            if not re.fullmatch(r"[0-9a-f]{40}", source_commit) or source_commit != context_commit:
                errors.append(
                    f"{app_dir.name}: upstream sourceCommit must match the source-build context"
                )
            if delivery.get("sourceBuild") != "upstream-dockerfile":
                errors.append(
                    f"{app_dir.name}: source builds must declare delivery.sourceBuild as upstream-dockerfile"
                )
            reproducible_build = delivery.get("reproducibleBuild")
            if not isinstance(reproducible_build, bool):
                errors.append(
                    f"{app_dir.name}: source builds must declare delivery.reproducibleBuild"
                )
            elif review_status == "approved" and reproducible_build is not True:
                errors.append(
                    f"{app_dir.name}: approved source builds must be reproducible"
                )
        elif not image and service_name != "app_proxy":
            errors.append(f"{app_dir.name}: service {service_name} requires a pinned image or source build")

        volumes = service.get("volumes") if isinstance(service.get("volumes"), list) else []
        for volume in volumes:
            source = ""
            if isinstance(volume, str):
                source = volume.split(":", 1)[0].strip()
            elif isinstance(volume, dict) and str(volume.get("type") or "").strip() == "bind":
                source = str(volume.get("source") or "").strip()
            if source.startswith(("./", "../")):
                errors.append(
                    f"{app_dir.name}: service {service_name} relative bind source is not installed; "
                    "use the APP_DATA_DIR data-seeding contract"
                )

    for path in app_dir.rglob("*"):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in FORBIDDEN_PAYLOAD_SUFFIXES:
            errors.append(f"{app_dir.name}: third-party payload files are not allowed ({path.relative_to(app_dir)})")
        elif path.name not in ALLOWED_APP_BASENAMES and suffix not in ALLOWED_APP_SUFFIXES:
            errors.append(f"{app_dir.name}: unsupported recipe file type ({path.relative_to(app_dir)})")
        if path.stat().st_size > MAX_APP_FILE_BYTES:
            errors.append(f"{app_dir.name}: recipe file exceeds {MAX_APP_FILE_BYTES} bytes ({path.relative_to(app_dir)})")
        if suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if FORBIDDEN_ASSOCIATIONS.search(text):
            errors.append(f"{app_dir.name}: prohibited inherited-store association in {path.relative_to(app_dir)}")

    return errors


def published_ports(app_dir: Path) -> list[tuple[int, str]]:
    """Return every host port published by an app's Compose recipe."""
    compose = load_yaml(app_dir / "docker-compose.yml")
    services = compose.get("services") if isinstance(compose.get("services"), dict) else {}
    result: list[tuple[int, str]] = []
    for service_name, service in services.items():
        if not isinstance(service, dict):
            continue
        ports = service.get("ports") if isinstance(service.get("ports"), list) else []
        for value in ports:
            if isinstance(value, dict):
                published = value.get("published")
                if isinstance(published, int) or str(published or "").isdigit():
                    result.append((int(published), str(service_name)))
                continue
            raw = str(value).split("/", 1)[0].strip()
            match = re.search(r"(?:^|:)([0-9]+)(?:-[0-9]+)?:[0-9]+(?:-[0-9]+)?$", raw)
            if match:
                result.append((int(match.group(1)), str(service_name)))
    return result


def validate_unique_ports(app_dirs: list[Path]) -> list[str]:
    owners: dict[int, list[str]] = {}
    for app_dir in app_dirs:
        if not (app_dir / "docker-compose.yml").is_file():
            continue
        try:
            entries = published_ports(app_dir)
        except Exception as exc:
            return [f"{app_dir.name}: cannot inspect published ports: {exc}"]
        for port, service_name in entries:
            owners.setdefault(port, []).append(f"{app_dir.name}/{service_name}")
    return [
        f"host port {port} is published more than once ({', '.join(port_owners)})"
        for port, port_owners in sorted(owners.items())
        if len(port_owners) > 1
    ]


def main() -> int:
    unexpected_args = [arg for arg in sys.argv[1:] if arg != "--allow-pending"]
    if unexpected_args:
        print(f"Unknown argument(s): {', '.join(unexpected_args)}", file=sys.stderr)
        return 2
    allow_pending = "--allow-pending" in sys.argv[1:]
    app_dirs = sorted(
        path for path in ROOT.iterdir()
        if path.is_dir() and path.name not in IGNORED and not path.name.startswith(".")
    )
    errors = [error for app_dir in app_dirs for error in validate_app(app_dir, allow_pending)]
    errors.extend(validate_unique_ports(app_dirs))
    if errors:
        print("5tratStore validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    pending_count = sum(
        1
        for app_dir in app_dirs
        if load_yaml(app_dir / "5tratstore-review.yml").get("status") == "pending"
    )
    approved_count = len(app_dirs) - pending_count
    suffix = f", {pending_count} pending" if pending_count else ""
    print(f"5tratStore validation passed: {approved_count} approved app(s){suffix}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
