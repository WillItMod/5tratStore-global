# Licence and image record

- Upstream: Prometheus Alertmanager 0.33.1 — Apache-2.0
  - Source: https://github.com/prometheus/alertmanager/tree/v0.33.1
  - Licence: https://github.com/prometheus/alertmanager/blob/v0.33.1/LICENSE
  - Release: https://github.com/prometheus/alertmanager/releases/tag/v0.33.1
  - Docker documentation: https://github.com/prometheus/alertmanager#docker-images
- Container: official upstream `quay.io/prometheus/alertmanager:v0.33.1`
  - Multi-architecture index digest:
    `sha256:9e082985f56f4c8c9f724e18f2288c6708f472e56a5286b8863d080434ea065d`
  - Verified platforms: `linux/amd64`, `linux/arm64`.
- Initialisation helper: Alpine Linux `alpine:3.22.1`
  - Multi-architecture index digest:
    `sha256:4bcff63911fcb4448bd4fdacec207030997caf25e9bea4045fa6c8c44de311d1`
  - Licence information: https://www.alpinelinux.org/about/
- The icon is loaded directly from Prometheus's official project asset:
  https://raw.githubusercontent.com/prometheus/prometheus/v3.13.2/documentation/images/prometheus-logo.svg
- `screenshots/overview.png` was captured during the isolated 5tratumOS
  compatibility test. It shows the unmodified upstream Alertmanager UI.

The recipe runs the unmodified official upstream image. It does not host,
mirror, alter or redistribute Alertmanager source code or images.
