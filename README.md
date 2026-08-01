# 5tratStore GLOBAL

The 5tratumOS-owned catalogue for legally cleared, compatibility-tested
third-party applications.

This repository started empty by design and remains deliberately small. It is
not a mirror or fork of another app store. Every app is independently packaged
from its original upstream project and must pass the review gate in
[STORE_POLICY.md](STORE_POLICY.md).

## Delivery model

GLOBAL stores recipes only: original listing metadata, small configuration and
initialisation files, notices, review evidence, and store-owned test captures.
It does **not** contain or serve third-party application source, container
images, executables, archives, or build outputs. When a user presses Install,
their own node pulls a digest-pinned image or a commit-pinned source tree
directly from the original upstream publisher. A source build is permitted only
when it uses the upstream project's own Dockerfile unchanged and remains local
to the user's node. The resulting runtime is never stored by this repository.

Projects without either a suitable original upstream runtime artifact or an
upstream-maintained Dockerfile are held as candidates. GLOBAL will not create,
mirror, or host a substitute image merely to add another app.

## Approved catalogue

- **Bitcoin and mining:** Alby Hub, LNbits, HashWatcher Remote Monitoring
  Setup, Node-RED and Eclipse Mosquitto™.
- **Metrics, logs and alerts:** Uptime Kuma, Prometheus, Grafana, ntfy,
  Alertmanager, InfluxDB, Telegraf, Grafana Loki, Prometheus Pushgateway,
  VictoriaMetrics, Beszel Hub, VictoriaLogs, OpenTelemetry Collector, Gatus
  and Mailpit.
- **Private operations and storage:** Tailscale, Syncthing, rclone, NATS,
  SeaweedFS, Gitea, SearXNG, PrivateBin and linkding.
- **Other independently reviewed tools:** Actual Budget.

There are 30 approved recipes. Exact versions and approval evidence live beside
each package and are enforced by the validator.

## Pending review

- Arkade Wallet — held until the OS provides a unique secure app origin and the
  upstream high-severity dependency advisory is fixed.
- DeepSea Dashboard — held for reproducible upstream build inputs and frontend
  security fixes before Proxmox and recovery testing.
- Bitaxe Sentry — held for reproducible upstream build inputs and an upstream
  fix that stops notification credentials entering logs.
- IT-Tools — direct upstream multi-architecture release image; local ARM
  lifecycle passed but the stale base image has fixable critical findings, so
  it remains held before any Proxmox or release test.

Every approved recipe passed the lifecycle declared in its review record.
Approval evidence lives beside each recipe and the default validator rejects
any unapproved directory. Maintainers can use `--allow-pending` for structural
checks on a draft branch; that flag is never used for release validation.

## Catalogue contract

Each app lives in a top-level directory and must include:

- `5tratstore-app.yml` — original 5tratStore listing metadata.
- `docker-compose.yml` — pinned runtime definition; floating `latest` tags are rejected.
- `5tratstore-review.yml` — signed-off legal and compatibility evidence.
- `LICENSES.md` — applicable licences, notices, and artifact provenance.
- `icon` — an original local icon or a direct HTTPS link to the upstream
  project's official icon; its provenance is documented in the review record.

Every approved review declares `delivery.mode: direct-upstream-artifact`,
`storePayload: recipe-only`, and `mirrorsThirdPartyPayload: false`.

Listing copy identifies the upstream product faithfully. Where available,
logos are loaded directly from the upstream project's official public assets;
the store does not substitute 5tratumOS artwork. Gallery images are either
direct upstream media or screenshots captured during compatibility testing.

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
