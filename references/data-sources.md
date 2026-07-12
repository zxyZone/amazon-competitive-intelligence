# Data Sources

## Source Priority

1. SellerSprite MCP, SIF MCP, or Sorftime MCP.
2. Manual exports from SellerSprite, SIF, Sorftime, Keepa, or Amazon frontend research.
3. Screenshots, copied page text, ASIN links, and user observations.
4. User-authorized web search for Google, TikTok, YouTube, Reddit, deal sites, or brand pages.

Do not block analysis when data is incomplete. Downgrade confidence and list the missing evidence.

## Minimum Inputs

Required:

- Marketplace, such as US, CA, UK, DE, JP.
- One ASIN, a list of ASINs, or a category/keyword export.
- At least one structured source: MCP output, CSV, JSON, XLSX, or pasted table.

Strongly recommended:

- ASIN detail: title, brand, seller, category path, price, rating, reviews, launch date, fulfillment, variation count.
- Competitor table: ASIN, title, brand, price, monthly units, revenue, BSR, reviews, rating, review growth, sales growth.
- Traffic keyword table: keyword, search volume, purchases, purchase rate, natural rank, ad rank, PPC bid, traffic share.
- Historical trend table: price, coupon, BSR, sales, revenue, reviews, offers, Buy Box over time.
- Review export: title, body, star, date, VP/Vine/media flags.
- Listing evidence: title, bullets, A+, image screenshots, video, variation structure.

## MCP Field Targets

SellerSprite-like MCP targets:

- `asin_detail`: product facts, seller, category, price, rating, reviews, badges, variations, listing quality.
- `asin_detail_with_coupon_trend` or `asin_coupon_trend`: coupon and effective price signals.
- `asin_prediction`: sales, revenue, price, BSR trend across recent months.
- `competitor_lookup`: batch products, units, revenue, BSR, review growth, seller, brand, category.
- `traffic_keyword`: natural rank, ad rank, traffic share, PPC bid, searches, purchases.
- `traffic_listing`: related competitors and association strength.
- `review`: review text and rating signals.
- `google_trend`: external Google demand trend when available.

SIF or Sorftime MCP outputs should be mapped to the same evidence buckets even if their field names differ.

## Manual Import Boundary

Accepted manual files:

- CSV, TSV, JSON, XLSX exports.
- Keepa CSV/XLSX or screenshots.
- Amazon page screenshots or copied frontend text.
- Google Trends screenshots or exports.
- Deal site, TikTok, YouTube, Reddit, Google search evidence supplied by the user.

Ask before using live web search. Ask before storing reports, pushing GitHub commits, writing Feishu records, or scheduling monitoring.

## Missing Data Handling

Use this downgrade rule:

- Missing price history: promotion and lifecycle confidence cannot exceed medium.
- Missing keyword/ad data: ad strategy confidence cannot exceed low/medium.
- Missing review history: product quality and lifecycle confidence cannot exceed medium.
- Missing historical snapshots: follow-up review becomes a current-state report, not a change report.
- Missing offsite evidence: offsite conclusions must be "suspected" only.
