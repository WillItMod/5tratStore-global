# Licence, service and image record

- Upstream client: Tailscale 1.98.10 — BSD-3-Clause
  - Source: https://github.com/tailscale/tailscale/tree/v1.98.10
  - Licence: https://github.com/tailscale/tailscale/blob/v1.98.10/LICENSE
  - Release: https://github.com/tailscale/tailscale/releases/tag/v1.98.10
- Container: official upstream `tailscale/tailscale:v1.98.10`
  - Multi-architecture index digest: `sha256:cdf5612ded5be1344f1a704b8c5e53496db97376bb533e5e15f141e48bf60cc0`
  - Container parameters: https://tailscale.com/docs/features/containers/docker/docker-params
- Initialisation helper: Alpine Linux `alpine:3.22.1`
  - Multi-architecture index digest: `sha256:4bcff63911fcb4448bd4fdacec207030997caf25e9bea4045fa6c8c44de311d1`
  - Licence information: https://www.alpinelinux.org/about/
- Hosted coordination service:
  - Terms: https://tailscale.com/terms
  - Legal hub: https://tailscale.com/legal
- The icon is loaded directly from Tailscale's official public asset:
  https://tailscale.com/favicon.svg
- `screenshots/setup.png` was captured during the isolated 5tratumOS
  compatibility test and shows the unmodified upstream setup screen.

Tailscale is a registered trademark of Tailscale Inc. The name and direct
official icon are used only to identify the unmodified upstream client and
service selected by the user. This independent recipe is not affiliated with
or endorsed by Tailscale Inc.

The recipe runs the unmodified official upstream image. Corresponding source is
available from the exact tagged source link above.
