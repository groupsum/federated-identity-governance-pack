<div align="center">

# federated-identity-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/federated-identity-governance-pack.svg)](https://pypi.org/project/federated-identity-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/federated-identity-governance-pack.svg)](https://pypi.org/project/federated-identity-governance-pack/)
[![License](https://img.shields.io/pypi/l/federated-identity-governance-pack.svg)](https://pypi.org/project/federated-identity-governance-pack/)
[![CI](https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/ci.yml)
[![Publish](https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/publish.yml)

</div>

Governance for federation assurance, IdP and RP trust, OIDC and SAML assertions, metadata, keys, subject identifiers, attribute release, and federation audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `federated-identity-governance-pack` is an installable SSOT governance pack for Federated Identity. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for federated identity, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`federated-identity-governance-pack`](https://pypi.org/project/federated-identity-governance-pack/)
- GitHub package repository: [`groupsum/federated-identity-governance-pack`](https://github.com/groupsum/federated-identity-governance-pack)
- Import package: `federated_identity_governance_pack`
- 4 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:federated-identity`
- PyPI package: `federated-identity-governance-pack`
- Import package: `federated_identity_governance_pack`
- GitHub repository: [groupsum/federated-identity-governance-pack](https://github.com/groupsum/federated-identity-governance-pack)
- Reservation owner: `extension-pack:federated-identity-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Federated Identity

## Authority Sources

- [NIST SP 800-63C-4: Federation and Assertions](https://pages.nist.gov/800-63-4/sp800-63c.html)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [OASIS SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/)

## Included ADRs

- [`adr:fal-governs-federation-assertion-protection`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1000-fal-governs-federation-assertion-protection.yaml) - FAL Governs Federation Assertion Protection
- [`adr:federation-assertions-carry-identity-facts-not-application-permissions`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1001-federation-assertions-carry-identity-facts-not-application-permissions.yaml) - Federation Assertions Carry Identity Facts Not Application Permissions
- [`adr:federation-trust-metadata-and-key-rotation-are-explicit`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1002-federation-trust-metadata-and-key-rotation-are-explicit.yaml) - Federation Trust Metadata And Key Rotation Are Explicit
- [`adr:subject-identifiers-and-attribute-release-are-profiled`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1003-subject-identifiers-and-attribute-release-are-profiled.yaml) - Subject Identifiers And Attribute Release Are Profiled

## Included SPECs

- [`spc:federation-assurance-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2000-federation-assurance-contract.yaml) - Federation Assurance Contract
- [`spc:oidc-id-token-validation-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2001-oidc-id-token-validation-contract.yaml) - OIDC Id Token Validation Contract
- [`spc:oidc-userinfo-and-authentication-claims-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2002-oidc-userinfo-and-authentication-claims-contract.yaml) - OIDC Userinfo And Authentication Claims Contract
- [`spc:saml-assertion-validation-profile-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2003-saml-assertion-validation-profile-contract.yaml) - SAML Assertion Validation Profile Contract
- [`spc:federation-registration-metadata-and-key-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2004-federation-registration-metadata-and-key-contract.yaml) - Federation Registration Metadata And Key Contract
- [`spc:federated-subject-attribute-release-and-audit-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2005-federated-subject-attribute-release-and-audit-contract.yaml) - Federated Subject Attribute Release And Audit Contract

## Install With uv

```bash
uv add federated-identity-governance-pack
uv add ssot-registry federated-identity-governance-pack
```

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect federated_identity_governance_pack
uvx --from ssot-registry ssot pack preflight . federated_identity_governance_pack --all
uvx --from ssot-registry ssot pack sync . federated_identity_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from federated_identity_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-federation-assurance-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/federated-identity-governance-pack](https://github.com/groupsum/federated-identity-governance-pack)
- PyPI package: [federated-identity-governance-pack](https://pypi.org/project/federated-identity-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the federated identity governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
