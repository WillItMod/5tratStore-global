# Pearl by Kraskus GLOBAL review

Request: https://github.com/WillItMod/5tratStore-global/issues/39

Submitted version: 0.6.5. Review target: linux/amd64 only. Status: approved for the tested amd64 release on 5tratumOS v0.8.53-dev.

## Packaging decisions

- Every runtime image has its verified tag and immutable digest; platform is explicitly linux/amd64.
- Browser access is through the authenticated 5tratumOS proxy with a loopback-only listener.
- Corrected listing APP_PORT from 80 to the actual UI listener 8080.

All persistent mounts remain under APP_DATA_DIR and retain the publisher's directory layout. No Docker socket, host networking, privileged mode or host devices are introduced. Private RPC and control endpoints are not published. One-shot initialization and any explicitly declared capabilities retain their upstream purpose. Mining destinations must be configured by the installer; no user address, key or seed is supplied by the recipe. No mining is activated during store testing.

## Qualification scope

Install and render with the real 5tratumOS lifecycle; verify browser/API readiness and authenticated portal access; restart; update/recreate with state and synthetic recovery sentinels retained; back up and restore disposable state; uninstall without purging and confirm data preservation; verify no unexpected host listeners. Record exact OS version, image digests and results. Full chain synchronization and real mining/reward tests must be reported separately and never inferred from a working dashboard.


## Observed results — 17 November 2026

The real 5tratumOS CLI installed the candidate through an isolated custom review catalogue. The official containers started with disposable persistent data. The dashboard and live `/api/state` returned HTTP 200 after initial start, restart, same-version update and full stopped-data restore. State was not simulated, mining remained disabled and no user payout address was configured. The authenticated portal served the app HTML, API and JavaScript/CSS; unauthenticated access required login.

The test saved and restored the complete stopped test directory, preserved a synthetic recovery sentinel through update and restore, and uninstalled without purging data. Container exit events contained no forced-kill exit 137. No existing mining app was selected for a lifecycle operation. The small `qualification.json` record contains the exact image references, step outcomes, portal checks and recipe fingerprint; it contains no credentials, wallet material, databases or runtime logs.

This verifies catalogue integration and application lifecycle on one amd64 5tratumOS v0.8.53-dev host. It does not claim completed mainnet synchronization, physical miner validation, mined rewards, reward settlement or migration of a real historical wallet. The update test recreates the submitted version; it is not a cross-version migration test. ARM is unsupported by the submitted Kraskus images.
