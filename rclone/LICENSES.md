# Licence and image record

- Upstream: rclone 1.75.0 — MIT
  - Source: https://github.com/rclone/rclone/tree/v1.75.0
  - Licence: https://github.com/rclone/rclone/blob/v1.75.0/COPYING
  - Release: https://github.com/rclone/rclone/releases/tag/v1.75.0
- Official upstream image: `rclone/rclone:1.75.0`
  - Multi-architecture digest: `sha256:b06aed988cf5967de7c25be5925240983981c757f4ed1ac9d2fa659d51d60548`
- Icon is loaded directly from the upstream project:
  https://raw.githubusercontent.com/rclone/rclone/v1.75.0/graphics/logo/svg/logo_symbol_color.svg
- The upstream `--rc-web-gui` option obtains its Web UI from the rclone
  project's published release when it is first started. That runtime fetch is
  initiated by the original upstream binary on the user's node; no Web UI
  assets are stored, served, or mirrored by this repository.

The recipe uses the unmodified upstream image and does not host, mirror, alter
or redistribute upstream application code or images.
