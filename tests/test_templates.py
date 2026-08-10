from __future__ import annotations

import json
from pathlib import Path
import unittest

from federated_identity_governance_pack import (
    __pypi_package_name__,
    __ssot_package_name__,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)

ADR_FIELDS = {
    "schema_version",
    "kind",
    "id",
    "number",
    "slug",
    "title",
    "status",
    "origin",
    "summary",
    "body",
    "decision_date",
    "references",
    "supersedes",
    "superseded_by",
    "status_notes",
    "tags",
}
SPEC_FIELDS = ADR_FIELDS | {"spec_kind", "adr_ids"}
ADR_REQUIRED = {"schema_version", "kind", "id", "number", "slug", "title", "status", "origin", "summary", "body"}
SPEC_REQUIRED = ADR_REQUIRED | {"spec_kind", "adr_ids"}
STATUSES = {"draft", "in_review", "accepted", "rejected", "superseded", "withdrawn", "retired"}
ORIGINS = {"ssot-core", "ssot-origin", "extension-pack", "repo-local"}
SPEC_KINDS = {"normative", "operational", "governance", "local-policy"}


class GovernancePackManifestTests(unittest.TestCase):
    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("federated-identity-governance-pack", __ssot_package_name__)
        self.assertEqual("federated-identity-governance-pack", __pypi_package_name__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("federated-identity-governance-pack", metadata["ssot_package_name"])
        self.assertEqual("pack:federated-identity", metadata["origin"]["id"])
        self.assertEqual("federated_identity_governance_pack", metadata["origin"]["import_name"])
        self.assertEqual("governance-pack", metadata["origin"]["kind"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:federated-identity-governance-pack", metadata["trust"]["reservation_owner"])
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        self.assertEqual("1.0.0", load_pack_schema_version())

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("federated-identity-governance-pack", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual(4, len(manifest["documents"]["adr"]))
        self.assertEqual(6, len(manifest["documents"]["spec"]))

    def test_packaged_adr_documents_are_downstream_portable(self) -> None:
        adr_manifest = load_document_manifest("adr")
        self.assertEqual("adr:fal-governs-federation-assertion-protection", adr_manifest[0]["id"])
        for row in adr_manifest:
            text = read_packaged_document_text("adr", row["filename"])
            self.assertNotIn("pack:", text)
            self.assertNotIn("This pack", text)

    def test_packaged_spec_documents_are_downstream_portable(self) -> None:
        spec_manifest = load_document_manifest("spec")
        self.assertEqual("spc:federation-assurance-contract", spec_manifest[0]["id"])
        for row in spec_manifest:
            text = read_packaged_document_text("spec", row["filename"])
            self.assertNotIn("pack:", text)
            self.assertNotIn("This pack", text)

    def test_readme_conforms_to_governance_pack_contract(self) -> None:
        readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
        required_sections = ['## Answer Engine Summary', '## What This Governance Pack Provides', '## Pack Metadata', '## Domain Focus', '## Authority Sources', '## Included ADRs', '## Included SPECs', '## Install With uv', '## Use With The SSOT Registry CLI', '## Programmatic Usage', '## Resources', '## Normative Ownership Boundary']
        positions = [readme.index(section) for section in required_sections]
        self.assertEqual(positions, sorted(positions))
        metadata = load_pack_metadata()
        self.assertIn(f"https://pypi.org/project/{metadata['origin']['package_name']}/", readme)
        self.assertIn(metadata["origin"]["repository"], readme)
        self.assertIn(metadata["origin"]["import_name"], readme)
        self.assertIn(metadata["origin"]["id"], readme)
        self.assertIn(metadata["trust"]["reservation_owner"], readme)
        for kind in ("adr", "spec"):
            for row in load_document_manifest(kind):
                self.assertIn(row["id"], readme)
                self.assertIn(row["filename"], readme)

    def test_packaged_documents_use_only_canonical_fields(self) -> None:
        for row in load_document_manifest("adr"):
            payload = json.loads(read_packaged_document_text("adr", row["filename"]))
            self.assertEqual(set(payload), set(payload) & ADR_FIELDS)
            self.assertTrue(ADR_REQUIRED <= set(payload))
            self.assertEqual("adr", payload["kind"])
            self.assertIn(payload["status"], STATUSES)
            self.assertIn(payload["origin"], ORIGINS)
            self.assertIsInstance(payload["summary"], str)
            self.assertIsInstance(payload["body"], str)
            self.assertTrue(all(isinstance(item, str) for item in payload["references"]))

        for row in load_document_manifest("spec"):
            payload = json.loads(read_packaged_document_text("spec", row["filename"]))
            self.assertEqual(set(payload), set(payload) & SPEC_FIELDS)
            self.assertTrue(SPEC_REQUIRED <= set(payload))
            self.assertEqual("spec", payload["kind"])
            self.assertIn(payload["status"], STATUSES)
            self.assertIn(payload["origin"], ORIGINS)
            self.assertIn(payload["spec_kind"], SPEC_KINDS)
            self.assertIsInstance(payload["adr_ids"], list)
            self.assertTrue(all(isinstance(item, str) for item in payload["references"]))


if __name__ == "__main__":
    unittest.main()
