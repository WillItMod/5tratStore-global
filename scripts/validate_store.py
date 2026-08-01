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
    "icon.png",
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
FORBIDDEN_ASSOCIATIONS = re.compile(r"umbrel", re.IGNORECASE)


def load_yaml(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict):
        raise ValueError("must contain a YAML object")
    return value


def validate_app(app_dir: Path) -> list[str]:
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
    if review.get("schemaVersion") != 1 or review.get("status") != "approved":
        errors.append(f"{app_dir.name}: review must be schemaVersion 1 and approved")
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

    compatibility = review.get("compatibility") if isinstance(review.get("compatibility"), dict) else {}
    if not compatibility.get("osVersions") or not compatibility.get("architectures"):
        errors.append(f"{app_dir.name}: tested OS versions and architectures are required")
    for field in sorted(TESTS):
        if compatibility.get(field) is not True:
            errors.append(f"{app_dir.name}: compatibility.{field} must be true")

    services = compose.get("services") if isinstance(compose.get("services"), dict) else {}
    if not services:
        errors.append(f"{app_dir.name}: compose services are required")
    for service_name, service in services.items():
        if not isinstance(service, dict):
            continue
        image = str(service.get("image") or "").strip()
        if image and (image.endswith(":latest") or ":" not in image.rsplit("/", 1)[-1] and "@sha256:" not in image):
            errors.append(f"{app_dir.name}: service {service_name} image must use a pinned tag or digest")

    for path in app_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if FORBIDDEN_ASSOCIATIONS.search(text):
            errors.append(f"{app_dir.name}: prohibited inherited-store association in {path.relative_to(app_dir)}")

    return errors


def main() -> int:
    app_dirs = sorted(
        path for path in ROOT.iterdir()
        if path.is_dir() and path.name not in IGNORED and not path.name.startswith(".")
    )
    errors = [error for app_dir in app_dirs for error in validate_app(app_dir)]
    if errors:
        print("5tratStore validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"5tratStore validation passed: {len(app_dirs)} approved app(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
