# JURY verification — 2026-11-26

- Template foundation: 1.3.0; original JURY commit: 7e46557c1a85bf9265f97277b3b51b347d577d33 (recoverable through Git history).
- Contract verified by TonAPI metadata: `-1:bf7e01ea11ccc2b302e99c112822f832aee254be7fd00ede5046379c63cc3796`; friendly form `Ef-_fgHqEczCswLpnBEoIvgyruJUvn_QDt5QRjecY8w3lr2i`; Jury Token / JURY / decimals 9. Workchain -1 is retained in normalization and snapshot identity checks.
- Source: https://tonapi.io/v2/jettons/-1:bf7e01ea11ccc2b302e99c112822f832aee254be7fd00ede5046379c63cc3796 . Description is attributed to metadata. Project page: https://telemarket.org/oracle/dao .
- Hero and section art: user attachment `libfile_b366f2e814848191b95bc0ab3b007a2f`, converted losslessly to WebP and embedded. No external image dependency.
- Market coverage: no verified pools configured. GeckoTerminal returned 404 for the exact token, STON.fi and DeDust APIs returned 403. This is an access/coverage limit, not evidence of no trading. No prices, market cap or seller statistics are fabricated. No Telegram channel was established; none was invented.
- Browser QA: desktop document width and scroll width 1348px; mobile iframe document width and scroll width 375px (390px outer viewport including scrollbar). No horizontal overflow. All images loaded. No missing local anchor targets. RU/EN controls, navigation, holder expansion 10 → 20, and partial-data rendering checked. Chart rendering checked in its unavailable state; real trade plotting cannot be verified without pool data.
- External links: GitHub returned 200; Telemarket, Oracle DAO and gram.org returned 403 during direct HTTP checks. Their availability remains unverified in this environment.
- Offline QA: 52 Python tests and 36 JavaScript tests passed; app syntax check, frozen reference integrity, standalone build and snapshot verification passed.
- Existing validate.yml and example scheduler registry retained. Added update.yml for workflow_dispatch, source-change refresh and atomic last-good publication. Live Cloudflare registration and a scheduled dispatch are not independently verified.
- Publishing to GitHub main does not upload a TON Storage bag or change TON DNS.

## Final packaged artifact

HTML bytes: 267710

SHA-256: `74e695bcf30f6deb9d289adbe8062ff16579d1ee5c5f431f7e3433705bd189c9`

Snapshot updated (Unix): 1795662504

Pending sections: domains, fragmentNumbers, pools, tradeHistory, trades. Domain and Fragment ownership enrichment was interrupted after the completed stages; no ownership claims were fabricated.
