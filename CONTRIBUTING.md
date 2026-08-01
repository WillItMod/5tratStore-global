# Contributing an app to 5tratStore GLOBAL

Thank you for helping build an independent catalogue for 5tratumOS. GLOBAL is
not a mirror of another store. Every submission must be created from the
original upstream project and must pass provenance, licence, security, and
5tratumOS lifecycle review before users can see it.

## The principles

1. **Upstream first.** Work from the original project repository, release, and
   documentation. Do not copy another app store's recipe, text, screenshots,
   metadata, or artwork.
2. **Rights before reach.** Popularity does not grant redistribution rights. A
   clear upstream licence or explicit written permission is mandatory.
3. **Fail closed.** A proposed app is not published while evidence or testing is
   incomplete. Maintainers alone change a review to `approved`.
4. **Least privilege.** Avoid privileged mode, host networking, Docker socket
   access, host mounts, and devices. If one is essential, disclose and justify
   it explicitly.
5. **Reproducible artifacts.** Pin container versions and multi-architecture
   index digests. Floating `latest` tags are rejected.
6. **Private and user-controlled defaults.** Do not silently upload telemetry,
   expose unauthenticated services, install companion apps, or alter the host.
7. **Honest compatibility.** Declare only versions and architectures actually
   tested. A working container elsewhere is not proof it works on 5tratumOS.

Read [STORE_POLICY.md](STORE_POLICY.md) before beginning.

## What makes a good submission

GLOBAL prioritises applications useful for mining, blockchain nodes, pools,
wallet infrastructure, payments, telemetry, monitoring, alerting, backups, and
secure remote operation. Maintained projects with original source, a clear
licence, and an official multi-architecture image are the easiest to review.

Do not submit:

- software produced specifically by a store vendor we are replacing;
- copied or mechanically rebranded store packages;
- projects without a licence or written distribution permission;
- floating or untraceable images;
- pirated, bypassed, cracked, or licence-key-evading software;
- packages that require undisclosed credentials, telemetry, privileges, or
  externally hosted services;
- placeholder recipes that have not been researched.

## Submission process

1. Check existing apps, open pull requests, and app requests to avoid duplicate
   work.
2. Fork this repository and create a branch named `app/<app-id>`.
3. Copy `templates/app/` to a new top-level directory named with a lowercase,
   stable app ID, for example `my-miner-monitor/`.
4. Write original listing text based on upstream facts.
5. Replace every `replace-me` value and add an original or explicitly licensed
   512×512 `icon.png`.
6. Record the exact upstream version, licence evidence, source link, official
   image tag and multi-architecture digest in `LICENSES.md`.
7. Keep `5tratstore-review.yml` at `status: proposed`, leave maintainer review
   fields empty, and leave lifecycle results false. Do not self-approve.
8. Run the local checks below and open a **draft pull request**.
9. Respond to review findings. Maintainers will perform the `.235` lifecycle
   test and record approval if every gate passes.

## Required package layout

```text
app-id/
├── 5tratstore-app.yml
├── 5tratstore-review.yml
├── LICENSES.md
├── docker-compose.yml
├── icon.png
└── data/                  # optional default configuration only
```

`data/` must contain configuration that may be copied into persistent app data.
Never commit credentials, API keys, wallet seeds, certificates, private keys,
personal addresses, databases, or runtime state.

## Recipe requirements

- Use `${APP_DATA_DIR}` for persistent files.
- Use `${APP_PASSWORD}` when an application needs a generated initial password.
- Declare an `app_proxy` service only for an HTTP application and point it to
  the internal application service and port.
- Run as a non-root UID/GID where upstream supports it.
- Add `security_opt: [no-new-privileges:true]` unless documented evidence shows
  it is incompatible.
- Pin every image by stable tag **and** `@sha256:<multi-architecture-index>`.
- Store no secrets in listing metadata or Compose defaults.
- Use a dedicated, non-conflicting host port allocated during review.

## Local checks

Install the validator dependency and run:

```bash
python3 -m pip install pyyaml==6.0.2
python3 scripts/validate_store.py
```

The final approval validator is intentionally fail-closed. A new proposal will
remain blocked until a maintainer has verified its rights record and completed
install, start, update, restart/recovery, and uninstall testing on 5tratumOS.

Before requesting review, also run:

```bash
docker compose -f app-id/docker-compose.yml config
git diff --check
```

## Maintainer review

Maintainers verify:

- original upstream identity and exact version;
- licence and notice obligations;
- container publisher and immutable digest;
- original or cleared listing text and artwork;
- network endpoints, secrets, mounts, devices, and privileges;
- persistent data ownership and recovery behaviour;
- install, start, HTTP/service readiness, update, restart, and uninstall;
- compatibility on each architecture claimed by the review record.

Approval is version-specific. Updates that change upstream ownership, licence,
images, privileges, or data behaviour return to review.

## Requesting an app instead

If you do not want to build the recipe, use the repository's
[Request an app form](https://github.com/WillItMod/5tratStore-global/issues/new?template=app-request.yml).
Five independent expressions of support prioritise review, but requests never
bypass legal, provenance, security, or compatibility checks.
