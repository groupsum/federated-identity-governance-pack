# federated-identity-governance-pack

Governance for federation assurance, IdP and RP trust, OIDC and SAML assertions, metadata, keys, subject identifiers, attribute release, and federation audit evidence.

## Package identity

- Pack ID: `pack:federated-identity`
- PyPI distribution: `federated-identity-governance-pack`
- Python import: `federated_identity_governance_pack`
- Reservation owner: `extension-pack:federated-identity-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add federated-identity-governance-pack
uv run ssot pack sync . federated_identity_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://pages.nist.gov/800-63-4/sp800-63c.html
- https://openid.net/specs/openid-connect-core-1_0.html
- https://docs.oasis-open.org/security/saml/v2.0/
