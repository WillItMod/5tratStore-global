# Licence, service and image record

- Upstream client: Tailscale 1.102.5 — BSD-3-Clause
  - Source: https://github.com/tailscale/tailscale/tree/v1.102.5
  - Licence: https://github.com/tailscale/tailscale/blob/v1.102.5/LICENSE
  - Release: https://github.com/tailscale/tailscale/releases/tag/v1.102.5
- Container: official upstream `tailscale/tailscale:v1.102.5`
  - Multi-architecture index digest: `sha256:c507f3a2a6ab1cabd8d809b98edeb41edbd5c3fb6ad9632ffd098b4c7d0b4065`
  - Container parameters: https://tailscale.com/docs/features/containers/docker/docker-params
- Initialisation helper: Alpine Linux `alpine:3.22.1`
  - Multi-architecture index digest: `sha256:4bcff63911fcb4448bd4fdacec207030997caf25e9bea4045fa6c8c44de311d1`
  - Licence information: https://www.alpinelinux.org/about/
- Hosted coordination service:
  - Terms: https://tailscale.com/terms
  - Legal hub: https://tailscale.com/legal
- The icon is the unmodified PNG from Tailscale's official public asset:
  https://tailscale.com/favicon.png
- `screenshots/setup.png` was captured during the isolated 5tratumOS
  compatibility test and shows the unmodified upstream setup screen.

Tailscale is a registered trademark of Tailscale Inc. The name and direct
official icon are used only to identify the unmodified upstream client and
service selected by the user. This independent recipe is not affiliated with
or endorsed by Tailscale Inc.

The recipe runs the unmodified official upstream image. Corresponding source is
available from the exact tagged source link above.

The official 768 × 768 PNG favicon is included byte-for-byte as `icon.png`
for the store listing and installed-app tile. Orbit loads textures through
fetch, which its same-origin connection policy blocks for external URLs.
Keeping this small identification asset on the node fixes both views without
loosening the OS content security policy. Upstream artwork is unchanged.

SHA-256: `680570c9090b604450792f68ceed10beeb33a69c9bccc2a92e398564c7075a5c`.

Node access uses host networking, NET_ADMIN, NET_RAW and /dev/net/tun. The
setup web service remains on loopback port 33016 behind OS authentication.
It does not enable subnet routes, exit-node use or Tailscale SSH automatically.
