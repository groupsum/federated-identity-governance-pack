# federated-identity-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>federated-identity-governance-pack</strong></p>
<p align="center">Governance for federation assurance, IdP and RP trust, OIDC and SAML assertions, metadata, keys, subject identifiers, attribute release, and federation audit evidence.</p>
<p align="center">
<a href="https://pypi.org/project/federated-identity-governance-pack/"><img alt="pypi: federated-identity-governance-pack" src="https://img.shields.io/pypi/v/federated-identity-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.0.dev2" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.0.dev2&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/federated-identity-governance-pack/"><img alt="Monthly PyPI downloads: federated-identity-governance-pack" src="https://img.shields.io/pypi/dm/federated-identity-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/README.md"><img alt="README hits: federated-identity-governance-pack" src="https://hits.sh/github.com/groupsum/federated-identity-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Governance for federation assurance, IdP and RP trust, OIDC and SAML assertions, metadata, keys, subject identifiers, attribute release, and federation audit evidence.

### Why This Package

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for federated identity, without copying those requirements into adjacent governance packs.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Federated Identity Governance.

### Features

**Included ADRs**

- [`adr:fal-governs-federation-assertion-protection`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1000-fal-governs-federation-assertion-protection.yaml) — FAL Governs Federation Assertion Protection
- [`adr:federation-assertions-carry-identity-facts-not-application-permissions`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1001-federation-assertions-carry-identity-facts-not-application-permissions.yaml) — Federation Assertions Carry Identity Facts Not Application Permissions
- [`adr:federation-trust-metadata-and-key-rotation-are-explicit`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1002-federation-trust-metadata-and-key-rotation-are-explicit.yaml) — Federation Trust Metadata And Key Rotation Are Explicit
- [`adr:subject-identifiers-and-attribute-release-are-profiled`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/adr/ADR-1003-subject-identifiers-and-attribute-release-are-profiled.yaml) — Subject Identifiers And Attribute Release Are Profiled

**Included SPECs**

- [`spc:federation-assurance-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2000-federation-assurance-contract.yaml) — Federation Assurance Contract
- [`spc:oidc-id-token-validation-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2001-oidc-id-token-validation-contract.yaml) — OIDC Id Token Validation Contract
- [`spc:oidc-userinfo-and-authentication-claims-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2002-oidc-userinfo-and-authentication-claims-contract.yaml) — OIDC Userinfo And Authentication Claims Contract
- [`spc:saml-assertion-validation-profile-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2003-saml-assertion-validation-profile-contract.yaml) — SAML Assertion Validation Profile Contract
- [`spc:federation-registration-metadata-and-key-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2004-federation-registration-metadata-and-key-contract.yaml) — Federation Registration Metadata And Key Contract
- [`spc:federated-subject-attribute-release-and-audit-contract`](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates/specs/SPEC-2005-federated-subject-attribute-release-and-audit-contract.yaml) — Federated Subject Attribute Release And Audit Contract

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

For a reproducible install of the [first PyPI prerelease](https://pypi.org/project/federated-identity-governance-pack/0.1.0.dev2/), use `python -m pip install federated-identity-governance-pack==0.1.0.dev2`.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add federated-identity-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install federated-identity-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add federated-identity-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/federated-identity-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from federated_identity_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:federated-identity"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:federated-identity` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/federated-identity-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from federated_identity_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:federation-assurance-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-federation-assurance-contract.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `federated-identity-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect federated_identity_governance_pack
uv run ssot pack preflight . federated_identity_governance_pack --all
uv run ssot pack sync . federated_identity_governance_pack --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `federated_identity_governance_pack` in SSOT Registry. Review reservation owner `extension-pack:federated-identity-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

This package is the canonical owner of the federated identity governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `federated_identity_governance_pack` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/federated-identity-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/federated-identity-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/federated-identity-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/federated-identity-governance-pack/blob/master/src/federated_identity_governance_pack/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/federated-identity-governance-pack)
- [Issues](https://github.com/groupsum/federated-identity-governance-pack/issues)
- [Repository](https://github.com/groupsum/federated-identity-governance-pack)
- [pypi: federated-identity-governance-pack](https://pypi.org/project/federated-identity-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/federated-identity-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:federated-identity`. The pack's reservation owner is `extension-pack:federated-identity-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [NIST SP 800-63C-4: Federation and Assertions](https://pages.nist.gov/800-63-4/sp800-63c.html)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [OASIS SAML 2.0](https://docs.oasis-open.org/security/saml/v2.0/)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/federated-identity-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/federated-identity-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
