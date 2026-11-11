# Mysterium Node for 5tratumOS

Proposed 5tratStore GLOBAL recipe for the official Mysterium Network provider
node.

The recipe intentionally keeps the integration small:

- pulls the pinned official Mysterium container directly from upstream;
- stores node identity and runtime state under `${APP_DATA_DIR}`;
- preserves the host-networking and `NET_ADMIN` requirements documented by
  upstream;
- starts the provider with Mysterium's required terms-acceptance flag;
- uses a pinned nginx helper to expose the upstream local Node UI through the
  5tratumOS application proxy;
- does not include custom dashboards, referral links, third-party branding,
  screenshots, binaries, runtime databases, credentials, or private keys.

## Security and provider notice

Mysterium's official Docker instructions require host networking and
`NET_ADMIN`. Running a provider node may route third-party traffic through the
host's public IP.

Users should review the upstream installation documentation and provider terms
before installing or operating the node.

## Maintainer review focus

The proposal intentionally remains fail-closed.

Maintainers should verify:

1. upstream licence and artifact provenance;
2. official container publisher and pinned digest;
3. host-network and `NET_ADMIN` requirements;
4. Node UI endpoint/proxy behavior;
5. persistent identity behavior;
6. install and start;
7. restart/recovery;
8. update;
9. uninstall;
10. amd64 compatibility.

Lifecycle fields remain false until maintainer testing is complete.
