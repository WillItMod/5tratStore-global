# 5tratStore GLOBAL

The 5tratumOS-owned catalogue for legally cleared, compatibility-tested
third-party applications.

This repository starts empty by design. It is not a mirror or fork of another
app store. Every app is independently packaged from its original upstream
project and must pass the review gate in [STORE_POLICY.md](STORE_POLICY.md).

## Catalogue contract

Each app lives in a top-level directory and must include:

- `5tratstore-app.yml` — original 5tratStore listing metadata.
- `docker-compose.yml` — pinned runtime definition; floating `latest` tags are rejected.
- `5tratstore-review.yml` — signed-off legal and compatibility evidence.
- `LICENSES.md` — applicable licences, notices, and artifact provenance.
- `icon.png` — artwork whose reuse rights are documented in the review record.

Run `python3 scripts/validate_store.py` before proposing an app.

## Channels

- MAIN contains ratified stable 5tratumOS and approved first-party releases.
- DEV contains previews and release candidates.
- GLOBAL, this repository, contains approved third-party applications.

User-supplied repositories remain separate Custom Stores and are not part of
5tratStore.
