# Licence and artifact record

## Mysterium Node 1.38.5

- Upstream project: Mysterium Node
- Publisher: Mysterium Network
- Source: https://github.com/mysteriumnetwork/node
- Licence: GNU General Public License version 3 (`GPL-3.0`)
- Licence evidence:
  https://github.com/mysteriumnetwork/node/blob/master/LICENSE
- Upstream Docker installation documentation:
  https://github.com/mysteriumnetwork/node/blob/master/INSTALL.md
- Provider terms repository:
  https://github.com/mysteriumnetwork/terms

This 5tratStore GLOBAL package is recipe-only. It does not host, mirror,
repackage, or redistribute the Mysterium Node binary or container image. The
user's 5tratumOS node pulls the pinned official upstream artifact when the user
chooses Install.

## Official Mysterium runtime container

- Image: `mysteriumnetwork/myst:1.38.5-alpine`
- Multi-architecture index digest:
  `sha256:49c6381a3efaa11c2ad9728df3c88bd2df6e061882f83e4983677eb90ee717c2`
- Publisher: Mysterium Network
- Registry:
  https://hub.docker.com/r/mysteriumnetwork/myst
- Upstream installation instructions:
  https://github.com/mysteriumnetwork/node/blob/master/INSTALL.md

The runtime image is pulled directly from the upstream publisher.

## nginx Node UI proxy

- Image: `nginx:1.27-alpine`
- Multi-architecture index digest:
  `sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10`
- Publisher: Docker Official Images / nginx
- Image documentation:
  https://hub.docker.com/_/nginx
- nginx licence:
  https://nginx.org/LICENSE

The nginx binary is unmodified. This proposal includes only an original nginx
configuration that proxies the local upstream Mysterium Node UI into the
5tratumOS application proxy.

## `data/nodeui-proxy/default.conf`

Original configuration created specifically for this 5tratumOS recipe.

It contains no credentials, private keys, wallet information, upstream source
code, or runtime state.

## `icon.png`

Original trademark-neutral catalogue artwork created specifically for this
submission.

The artwork uses a generic connected-node motif. It does not copy, trace,
incorporate, modify, or reproduce Mysterium Network, MystNodes, Kraskus,
5tratumOS, or another app-store logo.

The artwork is included only to identify this recipe in the catalogue without
implying sponsorship, endorsement, affiliation, or maintenance by the upstream
project.
