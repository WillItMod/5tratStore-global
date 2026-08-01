# 5tratStore GLOBAL

The 5tratumOS-owned catalogue for legally cleared, compatibility-tested
third-party applications.

This repository started empty by design and remains deliberately small. It is
not a mirror or fork of another app store. Every app is independently packaged
from its original upstream project and must pass the review gate in
[STORE_POLICY.md](STORE_POLICY.md).

## Approved catalogue

- Uptime Kuma 2.4.0 — availability monitoring for pools, nodes, miners, and services.
- Prometheus 3.13.2 — metrics collection for mining infrastructure.
- Grafana 13.1.0 — dashboards for miner, node, pool, and host metrics.
- ntfy 2.26.3 — private-by-default notifications for miner, node, pool, and system alerts.
- Eclipse Mosquitto™ 2.1.2 — loopback-only MQTT for miner and system telemetry.
- Node-RED 5.0.4 — authenticated, loopback-only automation for miner telemetry, alerts, and control flows.

Each recipe passed install, start, update, and uninstall testing on a supported
5tratumOS `v0.7.3` build or `v0.7.4` release candidate on amd64. Approval
evidence lives beside each recipe and the validator rejects any unapproved
directory.

## Catalogue contract

Each app lives in a top-level directory and must include:

- `5tratstore-app.yml` — original 5tratStore listing metadata.
- `docker-compose.yml` — pinned runtime definition; floating `latest` tags are rejected.
- `5tratstore-review.yml` — signed-off legal and compatibility evidence.
- `LICENSES.md` — applicable licences, notices, and artifact provenance.
- `icon.png` — artwork whose reuse rights are documented in the review record.

Run `python3 scripts/validate_store.py` before proposing an app.

Every app is linked to the repository's structured feedback form. Reports are
user-reviewed and user-submitted; 5tratumOS does not silently upload telemetry
or logs. Repeated install, runtime, update, or recovery failures can move an app
back to review or remove it from the catalogue.

The GLOBAL header also links to a structured **Request an app** form. A request
is prioritised for review after five independent expressions of support. Demand
sets review priority only; it never bypasses the licence, provenance, security,
relevance, or compatibility gates.

## Channels

- MAIN contains ratified stable 5tratumOS and approved first-party releases.
- DEV contains previews and release candidates.
- GLOBAL, this repository, contains approved third-party applications.

User-supplied repositories remain separate Custom Stores and are not part of
5tratStore.
