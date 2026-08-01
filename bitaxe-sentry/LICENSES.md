# Bitaxe Sentry notices

5tratStore GLOBAL contains no Bitaxe Sentry source or image. On install, Docker
fetches the reviewed commit from the original GitHub repository and builds its
upstream root Dockerfile locally on the user's node. The result is not uploaded,
mirrored or distributed by 5tratStore.

- Upstream source: https://github.com/zachchan105/bitaxe-sentry
- Reviewed release: `v0.8.0`
- Reviewed commit: `af7fcb34a3c451fbe503a73772300a38dec70931`
- Upstream licence: MIT
- Licence evidence: https://github.com/zachchan105/bitaxe-sentry/blob/af7fcb34a3c451fbe503a73772300a38dec70931/LICENSE
- Build definition: the upstream root `Dockerfile`, unchanged

The icon and gallery are loaded directly from files in the reviewed upstream
repository. Bitaxe and any associated names or marks remain the property of
their respective owners. Their appearance identifies the upstream application
and does not imply ownership or endorsement by 5tratumOS.

Miner addresses and an optional Discord webhook are supplied only by the user.
The recipe does not include credentials, discover devices automatically, or
send 5tratumOS telemetry. The upstream web interface loads Bootstrap assets
from jsDelivr, and its optional Discord and ntfy integrations contact the
services configured by the user.
