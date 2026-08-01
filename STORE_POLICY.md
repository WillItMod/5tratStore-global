# 5tratStore GLOBAL admission policy

An app is eligible only when all of the following are true:

1. The package is created from the original upstream project, not copied from
   another app store.
2. The catalogue identifies the upstream software licence and gives users a
   direct path to the original publisher's artifact. A recipe-only listing does
   not convey the application source or binary, so copyleft licences (including
   GPL and AGPL) are not by themselves a reason to reject an app. Where a
   third-party hosted service is involved, its own terms and jurisdiction
   restrictions are reviewed and disclosed.
3. 5tratStore GLOBAL is **recipe-only**. It never hosts, mirrors, vendors,
   repackages, or serves third-party application source, images, binaries,
   archives, or build outputs. Each user node pulls either a pinned runtime
   image or a commit-pinned source tree directly from the original upstream
   publisher when the user chooses Install.
4. Container images are pinned by version and digest. A source-build recipe is
   allowed only when the original upstream project supplies the Dockerfile: the
   HTTPS Git context must be pinned to a full commit, the upstream Dockerfile is
   used without a store-carried patch, and the resulting image is built only on
   the user's node. Its base images and dependency resolution must also be
   reproducible from the reviewed inputs; a pinned Git commit alone is not
   sufficient when its Dockerfile or package manifests float dependencies. The
   review records the delivery model, reproducibility result, source commit and
   upstream licence evidence.
5. Listing text accurately identifies the upstream product and does not imply
   that 5tratumOS created, owns, or endorses it. Screenshots are either direct
   upstream media or captured during compatibility testing.
6. Icons use an upstream project's official public asset directly where one is
   available. The exact source URL and any applicable brand notice are recorded
   without copying a separate app store's media catalogue.
7. The listing includes the upstream licence, version, source and attribution
   information needed to identify what the user elects to install. 5tratStore
   does not claim upstream work as its own or create a substitute source offer
   because it does not distribute the upstream work.
8. The app has been installed, started, updated, backed up and restored where
   applicable, and uninstalled on every declared architecture and OS version.
9. Network access, host mounts, device access, privileged mode, secrets, and
   persistent data locations have been reviewed and disclosed.
10. A named reviewer records approval in `5tratstore-review.yml`.

The user node will retain the upstream runtime artifact while the app is
installed, because that is what runs the application. That runtime cache is
user-owned node state, not content stored or served by 5tratStore.

If an upstream project provides neither a suitable official runtime artifact
nor an upstream-maintained Dockerfile, it stays a candidate. GLOBAL does not
solve that gap by building, modifying or hosting a substitute image. A local
build of the upstream project's own commit-pinned Dockerfile is not uploaded or
distributed by 5tratStore.

“Publicly visible” or “available on GitHub” is not sufficient evidence of a
right to use an upstream artifact, access an upstream service, or use project
branding in a store listing.

Approval applies only to the reviewed version. Material changes to images,
licensing, permissions, or upstream ownership require a new review.

This process is an engineering and provenance control, not a substitute for
professional legal advice where rights remain unclear.
