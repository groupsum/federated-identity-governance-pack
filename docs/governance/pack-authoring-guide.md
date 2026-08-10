# SSOT Registry Pack Authoring Guide

This template is intentionally generic and ships with empty ADR and SPEC manifests. A concrete pack should add domain-specific ADR and SPEC documents before publication.

## Required Decisions

- Define the governed domain in the first ADR.
- List the standards, policies, or product surfaces that are in scope.
- Keep watchlist and out-of-scope candidates visible when they are adjacent to the governed domain.
- Split detailed SPECs by behavior surface, not by implementation library.
- Avoid broad compliance claims until features, tests, claims, and evidence exist in downstream repositories.

## Required Package Updates

- Rename `src/ssot_registry_pack_template` to the import package for the new pack.
- Update `pyproject.toml` project metadata, URLs, keywords, and package-data keys.
- Keep `ssot-pack-contracts>=0.2.17,<0.3.0` as a runtime dependency.
- Update `src/<package_name>/metadata.json` for the concrete pack.
- Keep `src/<package_name>/__init__.py` bound through `ssot_pack_contracts.bind_pack_contract(__name__)`.
- Update `scripts/sync_packaged_docs.py` and `scripts/bump_version.py` package paths.
- Add ADR YAML resources under `src/<package_name>/templates/adr`.
- Add SPEC YAML resources under `src/<package_name>/templates/specs`.
- Regenerate manifest rows from those packaged resources with `scripts/sync_packaged_docs.py`.
- Update tests so they verify the exact ADR and SPEC IDs shipped by the pack, or keep the empty-manifest assertions until the first governed rows are added.

## Required Pack Contract Elements

- Ship `metadata.json` as import-package package data.
- Set `metadata.schema_version` to `1.0.0`.
- Set `metadata.origin.id` to a normalized `pack:*` identifier.
- Set `metadata.origin.kind` to `governance-pack`.
- Set `metadata.trust.origin` to `extension-pack`.
- Set `metadata.trust.reservation_owner` to `extension-pack:<pypi-package-name>`.
- Use normalized `metadata.documents` keys: `adr` and `spec`.
- Keep manifest `origin` as `extension-pack`.
- Keep manifest `reservation_owner` aligned with `metadata.trust.reservation_owner`.
- Keep manifest `minimum_schema_version` aligned with `metadata.compatibility.ssot_registry_schema`.
- Include SHA-256 hashes for every packaged document and let `ssot-pack-contracts` validate them at read time.
- Include contract tests for metadata, pack manifest, document IDs, and packaged document reads.

## Required README Elements

- Include badge rows for PyPI version, downloads, hits, Python versions, license, CI, and GitHub repository.
- Include a concise opening description naming the pack domain and governed surface.
- Include an audience statement for the teams that should use the pack.
- Include `What Is An SSOT Registry Pack?`, `Why This Pack Exists`, and `Domain Focus`.
- Include `Included ADRs` and `Included SPECs` with stable SSOT IDs.
- Include a standards, proposal, or target-review section when the pack starts with a seed review contract.
- Include `Install With uv`, `Install With The SSOT Registry Pack CLI`, and `Use With The SSOT Registry CLI`.
- Include `Programmatic Usage`.
- Include `Resources` links for the GitHub repository, PyPI package, and SSOT Registry.
- Keep README package names, import names, PyPI URLs, GitHub URLs, and workflow badge URLs aligned with the concrete pack.

## Required Python Support Surface

- Keep `requires-python`, Python classifiers, `uv.lock`, and CI matrix aligned.
- Current concrete packs support Python 3.10, 3.11, 3.12, 3.13, and 3.14.
- Keep publish workflow tooling on a stable Python unless the release tooling itself requires a broader matrix.

## Recommended Initial Document Set

- One ADR that defines the pack boundary and standards inclusion policy.
- One SPEC that defines target-review requirements.
- One SPEC per governed behavior surface once the target set is reviewed.
- One README section listing included ADRs and SPECs by stable SSOT ID.
