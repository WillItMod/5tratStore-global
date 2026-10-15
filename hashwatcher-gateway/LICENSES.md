# Permission, provenance and image record

- Upstream project: HashWatcher Gateway 1.3.1, Engineered Essentials
  - Source: https://github.com/gpena208777/hashwatcherhub
  - The upstream repository does not currently publish a software licence.
  - On 2026-08-01, Gabe, the project developer, gave the 5tratumOS owner
    permission to integrate this guided remote-monitoring setup. It is not
    described or presented as the HashWatcher companion app.
- Container: original upstream `hashwatcher/hashwatcher-gateway:1.3.1`
  - Multi-architecture index digest:
    `sha256:969cab8e6b61de8411ea1bc7b8d87d9f9c618306e8f5c945deea12e5c870e3ba`
  - Publisher: https://hub.docker.com/r/hashwatcher/hashwatcher-gateway
  - Verified platforms: `linux/amd64` and `linux/arm64`.
  - This build updates the bundled Tailscale client to 1.104.1.
- The icon is loaded directly from the project repository, with the same
  project-developer permission recorded for this integration:
  https://raw.githubusercontent.com/gpena208777/hashwatcherhub/main/hashwatcher-gateway/icon.png

The listing text and recipe are original. The recipe pulls and runs the exact,
unmodified upstream image directly on the user's node. 5tratStore does not
host, mirror, alter or redistribute upstream application code or images.
