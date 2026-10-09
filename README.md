# Energi Sehari-hari | Vijeron

An original, bilingual (Indonesian and English) household electricity literacy site for `energi.vijeron.com`.

## What ships

- Ten original guides in each language, each with a worked example, a limitation, and primary-source links.
- Two browser-only tools: appliance kWh and same-schedule comparison. Users enter their own electricity rate; the tools do not fetch tariffs or transmit inputs.
- Static, crawlable HTML; per-page canonicals, language alternates, descriptions, Article/WebPage JSON-LD, sitemap, robots.txt, and ads.txt.
- GA4 `G-79X7K7H4MJ` and AdSense publisher `ca-pub-6180580801533680` tags on content pages. Consent defaults denied; the Google Funding Choices message script is included. Ad serving depends on account approval and applicable user consent.

## Build

Requires Python 3.10+ and no third-party packages:

```powershell
python build.py
```

The command writes `dist/`. Commit `dist/` so Cloudflare Pages can deploy the repository with an empty build command and `dist` as the output directory.

## Editorial and measurement rules

- `articles.py` is the source of the original bilingual copy. Source links are references, not licenses to republish source text or images.
- Rebuild after editing copy; update `TODAY` in `build.py` only when the pages actually change.
- Do not replace user-entered rates with assumed national tariffs. Actual bills can include fixed charges, taxes, and tiers.
- GA4 events use tool name and language only, never inputs, computed costs, or kWh.
- Do not claim these guides are a certified home energy audit or that the estimates guarantee savings.

## Cloudflare Pages

Connect this repository as a Git-integrated Pages project. Set production branch `main`, build command empty, and output directory `dist`. Add `energi.vijeron.com` as a custom domain in Pages. If the zone is already on Cloudflare, Pages will offer to create the DNS record. Check the custom domain and HTTPS after deployment.
