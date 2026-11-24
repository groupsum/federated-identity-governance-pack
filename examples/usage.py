"""Find a specification and its downstream path in the installed manifest."""

from federated_identity_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:federation-assurance-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-federation-assurance-contract.yaml"
