# Jury Token Observatory

## О проекте / токене

JURY is the voting token of the Telemarket oracle DAO. Holders resolve disputed oracle outcomes on Telemarket prediction markets by voting with their tokens. JURY may also be used in future projects.

Самоописание из метаданных токена; заявления проекта не проверены независимо.

Источники (проверены 2026-11-26):

- <https://tonapi.io/v2/jettons/-1:bf7e01ea11ccc2b302e99c112822f832aee254be7fd00ede5046379c63cc3796>
- <https://telemarket.org/oracle/dao>

Generated from https://github.com/Freebielife/TON-Observatory-Template.

Run python3 -m scripts.refresh_observatory; python3 build.py; python3 verify.py.
Publish index.html in TON Sites only after independent on-chain verification.
The embedded snapshot contains observed on-chain sections; unavailable sections are explicitly listed in data/snapshot.json errors.
Only native TON swap pairs supported. Locks, staking and custom project NFT badges are configured through project.json and verified against TonAPI.
Configure your GitHub workflow scheduler before launch.

Foundation version: 1.3.0. Holders show 10, expandable to top 20.
`project.json` is the per-project specification. Contract/pool/precision changes require regenerating from the factory; do not reuse another token's snapshot.
Run `python3 build.py` for an atomic bundle and `build/report.json` size report.
No external fonts, scripts or images are needed to render the saved page. Fresh data checks and manual wallet lookups require network access.
Cloudflare dispatch registration and GitHub repository access remain separate deployment steps. No credentials go into HTML.

## JURY: verified scope (2026-11-26)

Exact raw master: `-1:bf7e01ea11ccc2b302e99c112822f832aee254be7fd00ede5046379c63cc3796`. Friendly address retains workchain -1. Decimals: 9, verified with TonAPI. The user-provided attachment is used for both hero and section artwork by explicit instruction.

No pools are configured: GeckoTerminal returned HTTP 404 for the exact token, while STON.fi and DeDust APIs returned HTTP 403. These failures do not establish absence of trading. No prices, sellers, trades or capitalization are fabricated. No verified Telegram channel was found; the official website and Oracle DAO links are used.

Existing validate.yml is retained. update.yml supports the existing external workflow_dispatch mechanism. The live Cloudflare scheduler registry is not modified, and its JURY registration cannot be independently verified here. Publication in main is distinct from uploading to TON Storage.
