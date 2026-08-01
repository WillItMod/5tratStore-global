# Candidate register

Research queue only. Presence in this file does **not** approve an app for
5tratStore. Approved apps appear as top-level package directories and must pass
the full review gate.

There is no public, independently verifiable per-app install telemetry for the
legacy catalogue. The initial queue therefore uses original-upstream adoption
signals (GitHub stars), maintenance recency, relevance to blockchain/mining,
and an initial repository licence signal. Stars are a prioritisation aid, not
proof of quality, compatibility, or legal clearance.

Snapshot: 2026-08-01. Every URL below is an original upstream repository.

| Candidate | Role | Upstream signal | Licence signal | Initial disposition |
|---|---|---:|---|---|
| Gleec Wallet (Komodo DeFi SDK) | Self-custodial multi-chain wallet and atomic-swap DEX | Current Gleec/Komodo product; release 0.9.5 | GPL-3.0; hosted-service terms separate | **Highest priority, delivery/security hold:** GPL is compatible with a recipe-only listing; require an official direct runtime artifact and HTTPS wallet delivery |
| Tailscale | Private encrypted networking between the user's devices | Current release 1.98.10 | BSD-3-Clause; hosted-service terms separate | **Approved:** 1.98.10 userspace recipe lifecycle-tested on amd64; user account, arm64 and Sol/high follow-up tracked |
| Uptime Kuma | Pool/node uptime monitoring | 89,693 stars | MIT | **Approved:** 2.4.0 recipe tested on amd64 |
| Netdata | Host and container monitoring | 79,968 | GPL-3.0 | Research; resource/security review needed |
| Grafana | Mining and node dashboards | 75,905 | AGPL-3.0 | **Approved:** direct upstream recipe lifecycle-tested on amd64 |
| Prometheus | Metrics collection | 65,402 | Apache-2.0 | **Approved:** 3.13.2 recipe tested on amd64 |
| Alertmanager | Alert grouping, routing, silencing and inhibition | Prometheus project | Apache-2.0 | **Approved:** 0.33.1 safe-default recipe tested on amd64 |
| ntfy | Private infrastructure notifications | 26,000+ | Apache-2.0 | **Approved:** 2.26.3 private-by-default recipe tested on amd64 |
| Node-RED | Miner telemetry and control automation | 23,476 | Apache-2.0 | **Approved:** 5.0.4 loopback-only recipe tested on amd64 |
| Eclipse Mosquitto™ | MQTT for miner telemetry | 11,086 | EPL-2.0 OR BSD-3-Clause | **Approved:** 2.1.2 loopback-only recipe tested on amd64 |
| InfluxDB | Time-series metrics and events | Current 2.7.12 release | Apache-2.0 | **Approved:** 2.7.12 unmodified upstream recipe lifecycle-tested on amd64; first-run setup is administrator-led |
| Telegraf | Local metrics collection agent | Current 1.39.2 release | MIT | **Approved:** 1.39.2 safe starter recipe lifecycle-tested on amd64; user configures any extra inputs/outputs |
| Electrum | Bitcoin wallet | 8,536 | MIT | Research; wallet/security review required |
| LND | Lightning node | 8,171 | MIT | Research; high state-loss risk |
| BTCPay Server | Bitcoin payment server | 7,679 | MIT | Research; complex multi-service package |
| Core Lightning | Lightning node | 3,080 | Repository requires manual licence review | Research; high state-loss risk |
| mempool | Bitcoin explorer and fee tools | 2,803 | Repository requires manual licence review | Research; complex dependencies |
| BTC RPC Explorer | Bitcoin node explorer | 1,791 | MIT | Research; likely early candidate |
| electrs | Electrum server | 1,382 | MIT | Research; node dependency and disk load |
| Esplora | Bitcoin explorer | 1,254 | MIT | Research; indexer dependency |
| LNbits | Lightning accounts and tools | 1,224 | MIT | **Approved:** 1.5.6 safe-default VoidWallet recipe lifecycle-tested on amd64; real backend/backup/arm64 follow-up tracked |
| RTL | Lightning node UI | 796 | MIT | Research; requires supported Lightning backend |
| Miningcore | Mining pool server | 790 | MIT | Hold: upstream repository is archived |
| ElectrumX | Electrum server | 567 | MIT | Research; storage/performance validation |
| Fulcrum | Electrum server | 489 | Repository requires manual licence review | Research; storage/performance validation |
| ThunderHub | LND node UI | 468 | MIT | Research; requires supported LND backend |
| Bitcoin-S | Bitcoin/Lightning application server | 381 | MIT | Research; lower adoption signal |

## Mining-focused gaps

These projects are more directly aligned with 5tratumOS than a generic home-server
catalogue. They were identified independently from their original upstreams and
should be prioritised even though their public adoption signals are smaller.

| Candidate | Role | Upstream signal | Licence signal | Initial disposition |
|---|---|---:|---|---|
| DATUM Gateway | Decentralised Bitcoin mining gateway | 146 stars; release 0.4.1beta | MIT licence file present; trademark excluded | Priority research; independent image build and amd64 miner/node interoperability required |
| Stratum V2 SRI | Stratum V2 protocol and mining infrastructure | 350 | Dual MIT/Apache-2.0 licence files present | Priority research; package only stable upstream components |
| ckpool | Bitcoin mining pool server | 24 | GPL-3.0 | Priority research; find an official direct runtime artifact and test pool safety |
| Public Pool | Solo mining pool UI/service | 17 | No repository licence found | Hold: obtain explicit upstream permission or a licence grant |
| HashWatcher Remote Monitoring Setup | Guided remote miner monitoring setup | Direct project-developer permission recorded 2026-08-01 | Proprietary; permission documented beside recipe | **Approved:** 1.3.0 recipe lifecycle-tested on amd64; real tailnet/miner, arm64 and Sol/high follow-up pending |

Upstream repositories, in the same order:

- https://github.com/louislam/uptime-kuma
- https://github.com/netdata/netdata
- https://github.com/grafana/grafana
- https://github.com/prometheus/prometheus
- https://github.com/binwiederhier/ntfy
- https://github.com/node-red/node-red
- https://github.com/eclipse-mosquitto/mosquitto
- https://github.com/spesmilo/electrum
- https://github.com/lightningnetwork/lnd
- https://github.com/btcpayserver/btcpayserver
- https://github.com/ElementsProject/lightning
- https://github.com/mempool/mempool
- https://github.com/janoside/btc-rpc-explorer
- https://github.com/romanz/electrs
- https://github.com/Blockstream/esplora
- https://github.com/lnbits/lnbits
- https://github.com/Ride-The-Lightning/RTL
- https://github.com/oliverw/miningcore
- https://github.com/spesmilo/electrumx
- https://github.com/cculianu/Fulcrum
- https://github.com/apotdevin/thunderhub
- https://github.com/bitcoin-s/bitcoin-s
- https://github.com/OCEAN-xyz/datum_gateway
- https://github.com/stratum-mining/stratum
- https://github.com/ckolivas/ckpool
- https://github.com/benjamin-wilson/public-pool-app

## Promotion order

1. Confirm the exact licence and trademark position from upstream primary sources.
2. Confirm official, pinned, multi-architecture container artifacts or create a reproducible build.
3. Write original metadata and obtain cleared artwork.
4. Review privileges, mounts, ports, secrets, and external connections.
5. Test install, start, restart, update, backup/restore, and uninstall on 5tratumOS.
6. Record approval and only then add the package to GLOBAL.
