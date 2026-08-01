# Permission, provenance and image record

- Upstream project: HashWatcher Gateway 1.3.0, Engineered Essentials
  - Source: https://github.com/gpena208777/hashwatcherhub
  - The upstream repository does not currently publish a software licence.
  - On 2026-08-01, Gabe, the project developer, gave the 5tratumOS owner
    permission to integrate this guided remote-monitoring setup. It is not
    described or presented as the HashWatcher companion app.
- Container: original upstream `hashwatcher/hashwatcher-gateway:1.3.0`
  - Multi-architecture index digest:
    `sha256:13af6f24a4e73b84ed173df90fd1489257316fbc433381f69dd9ed262645c9ef`
  - Publisher: https://hub.docker.com/r/hashwatcher/hashwatcher-gateway
  - Verified platforms: `linux/amd64` and `linux/arm64`.
- `icon.png` is original 5tratStore catalogue artwork covered by this
  repository's MIT licence. It does not use HashWatcher or Engineered
  Essentials artwork.

The listing text and recipe are original. The recipe pulls the exact upstream
image directly to the user's node and makes a local, runtime-only compatibility
copy of the gateway helper. 5tratStore does not host, mirror or redistribute
the upstream image or a modified image.
