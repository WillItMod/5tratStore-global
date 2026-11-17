# Kraskus admission — 17 November 2026

Scope: the ten maintainer-originated app requests #35–44. Seven add networks not already covered by the first-party catalogue and are included at the exact submitted versions. This is a recipe-only listing using official, unmodified publisher images. The publisher's fixed 1% developer allocation is preserved; Kaspa also retains its internal settlement wallet and transaction costs, and Zcash retains the required network allocations.

| Request | Application | Decision |
| --- | --- | --- |
| [#35](https://github.com/WillItMod/5tratStore-global/issues/35) | Monero 0.3.7 | Publish; new RandomX network coverage |
| [#36](https://github.com/WillItMod/5tratStore-global/issues/36) | Bitcoin Cash 0.5.13 | Exclude; overlaps AxeBCH |
| [#37](https://github.com/WillItMod/5tratStore-global/issues/37) | Bitcoin 0.5.7 | Exclude; overlaps AxeBTC |
| [#38](https://github.com/WillItMod/5tratStore-global/issues/38) | Kaspa 0.5.5 | Publish; new network coverage |
| [#39](https://github.com/WillItMod/5tratStore-global/issues/39) | Pearl 0.6.5 | Publish; new network coverage |
| [#40](https://github.com/WillItMod/5tratStore-global/issues/40) | CheetahCoin 0.6.3 | Publish; new network coverage |
| [#41](https://github.com/WillItMod/5tratStore-global/issues/41) | DigiByte 0.3.2 | Exclude; overlaps AxeDGB |
| [#42](https://github.com/WillItMod/5tratStore-global/issues/42) | XBT 0.3.4 | Publish; distinct BLAKE2b network, not ordinary Bitcoin |
| [#43](https://github.com/WillItMod/5tratStore-global/issues/43) | Bitcoin SV 0.6.4 | Publish; distinct network |
| [#44](https://github.com/WillItMod/5tratStore-global/issues/44) | Zcash 0.6.4 | Publish; new Equihash network coverage |

Overlap was checked against MAIN at `20e8cc628339baa2e979647058185efb85d3eb6d`, DEV at `18d92f5b0877bba721e47ffb8d3b9750af7ca0aa` and GLOBAL at `5795e812dab4567df9dcd7b1d106de8c864cddc3`. The revised packages have no declared host-port collision with those catalogues or one another. Monero and Bitcoin SV retain outbound peering without reserving their conventional inbound P2P host ports. XBT's miner-facing service joins a non-internal bridge. Pearl's browser metadata points to its actual 8080 listener. Monero's Python services and the CheetahCoin controller receive explicit signal-forwarding setup after forced stops were observed in the first test pass.

All 42 immutable references in the ten requests passed anonymous manifest retrieval, SHA-256 verification and tag correspondence checks. The seven admitted packages use 32 distinct references, all pulled directly from the named upstream publishers. The complete required Kraskus image sets are amd64-only; no ARM compatibility is claimed. Explicit platform fields and listing descriptions identify that limitation.

The real 5tratumOS CLI exercised installation, startup, restart, same-version update, stopped-data backup/restore and keep-data uninstall on an amd64 host running v0.8.53-dev. Each live API remained out of demo mode with mining disabled and no user payout address configured. Per-package qualification records include image references, outcomes and recipe fingerprints. Separate authenticated portal requests verified app HTML, JavaScript/CSS and live API data; anonymous requests required login.

These tests do not establish completed mainnet synchronization, physical miner compatibility, mined blocks, reward settlement or migration of a real historical wallet. Synthetic recovery sentinels and disposable state were used. The update test recreates the submitted version, not a previous application version.

The older [Mysterium proposal #31](https://github.com/WillItMod/5tratStore-global/pull/31) is outside this ten-request admission batch and remains pending its own host-network, NET_ADMIN, provider-terms and lifecycle review.
