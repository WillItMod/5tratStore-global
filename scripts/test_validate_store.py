from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from scripts.validate_store import validate_app, validate_unique_ports


SHA = "a" * 64


class ValidatorTests(unittest.TestCase):
    def write_yaml(self, path: Path, value: dict) -> None:
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def make_app(self, root: Path, name: str, port: int, volume: str | None = None) -> Path:
        app = root / name
        app.mkdir()
        self.write_yaml(
            app / "5tratstore-app.yml",
            {
                "id": name,
                "version": "1.0.0",
                "icon": "https://example.com/icon.svg",
            },
        )
        self.write_yaml(
            app / "5tratstore-review.yml",
            {
                "schemaVersion": 2,
                "status": "pending",
                "appId": name,
                "appVersion": "1.0.0",
                "reviewedAt": "2026-08-01",
                "reviewedBy": "test",
                "upstream": {
                    "sourceUrl": "https://github.com/example/app",
                    "license": "MIT",
                    "licenseEvidence": "https://github.com/example/app/blob/main/LICENSE",
                },
                "delivery": {
                    "mode": "direct-upstream-artifact",
                    "storePayload": "recipe-only",
                    "mirrorsThirdPartyPayload": False,
                },
                "rights": {
                    "packageOriginal": True,
                    "softwareDistributionCleared": True,
                    "containerUseCleared": True,
                    "listingTextCleared": True,
                    "artworkCleared": True,
                    "noticesIncluded": True,
                },
                "compatibility": {
                    "osVersions": ["pending"],
                    "architectures": ["amd64"],
                    "installTested": False,
                    "startTested": False,
                    "updateTested": False,
                    "backupTested": False,
                    "restoreTested": False,
                    "uninstallTested": False,
                },
            },
        )
        service = {
            "image": f"ghcr.io/example/app:1.0.0@sha256:{SHA}",
            "ports": [f"127.0.0.1:{port}:8080"],
        }
        if volume:
            service["volumes"] = [volume]
        self.write_yaml(app / "docker-compose.yml", {"services": {"app": service}})
        (app / "LICENSES.md").write_text("MIT\n", encoding="utf-8")
        return app

    def test_cross_app_port_collision_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = self.make_app(root, "first", 33001)
            second = self.make_app(root, "second", 33001)
            errors = validate_unique_ports([first, second])
            self.assertEqual(len(errors), 1)
            self.assertIn("33001", errors[0])

    def test_distinct_ports_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first = self.make_app(root, "first", 33001)
            second = self.make_app(root, "second", 33002)
            self.assertEqual(validate_unique_ports([first, second]), [])

    def test_relative_bind_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            app = self.make_app(Path(temporary), "relative-bind", 33001, "./seed.json:/seed.json:ro")
            errors = validate_app(app, allow_pending=True)
            self.assertTrue(any("relative bind source" in error for error in errors))

    def test_malformed_digest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            app = self.make_app(Path(temporary), "bad-digest", 33001)
            compose = yaml.safe_load((app / "docker-compose.yml").read_text(encoding="utf-8"))
            compose["services"]["app"]["image"] = "ghcr.io/example/app:1.0@sha256:abcd"
            self.write_yaml(app / "docker-compose.yml", compose)
            errors = validate_app(app, allow_pending=True)
            self.assertTrue(any("64-character SHA-256" in error for error in errors))

    def test_v2_approval_requires_recovery_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            app = self.make_app(Path(temporary), "recovery-gate", 33001)
            review_path = app / "5tratstore-review.yml"
            review = yaml.safe_load(review_path.read_text(encoding="utf-8"))
            review["status"] = "approved"
            for field in ("installTested", "startTested", "updateTested", "uninstallTested"):
                review["compatibility"][field] = True
            self.write_yaml(review_path, review)
            errors = validate_app(app)
            self.assertTrue(any("requires tested backup/restore" in error for error in errors))

            review["compatibility"]["backupNotApplicable"] = True
            review["compatibility"]["restoreNotApplicable"] = True
            self.write_yaml(review_path, review)
            errors = validate_app(app)
            self.assertFalse(any("requires tested backup/restore" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
