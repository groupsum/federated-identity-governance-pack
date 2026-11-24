"""Inspect the installed pack identity."""

from federated_identity_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:federated-identity"
print(metadata["origin"]["id"])
