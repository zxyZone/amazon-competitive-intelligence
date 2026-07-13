# Evidence Rules

## 中文导读

本文件是“证据到推断”的规则库。它不是绝对判定器，而是帮助 Codex 把价格、BSR、销量、Review、广告排名、关键词、Coupon、Deal、站外痕迹这些信号组合起来，形成有置信度的运营判断。

## Lifecycle Signals

Classify lifecycle with confidence, not certainty.

- New launch: short launch age, few reviews, unstable BSR, heavy ad rank, weak natural rank.
- Ramp-up: improving BSR, rising units, review velocity increasing, ad rank stronger than natural rank.
- Breakout: sharp BSR improvement, rising units and reviews, stable or only moderate discounting.
- Mature: stable sales, stable BSR, strong natural ranks, steady review growth, less aggressive promotion.
- Decline: worsening BSR, slowing reviews, falling units, frequent coupon or price cuts.
- Clearance or replacement: large discounts, coupon stacking, shrinking variation availability, reduced ad visibility, inconsistent stock.

Key consistency test:

```text
sales + BSR + reviews + price + ad rank
```

When they move together, confidence rises. When they diverge, explain the divergence.

## Promotion Signals

Direct evidence:

- Coupon amount or percentage.
- Effective price lower than list price.
- Deal badges, Lightning Deal, 7-Day Deal, Best Deal, Prime Exclusive Deal, Subscribe & Save.
- MCP or export fields that explicitly identify promotion activity.

Inferred evidence:

- Short price drop + rapid BSR improvement = likely flash deal or heavy short promotion.
- Multi-day low price + sustained BSR improvement = likely longer deal or rank push.
- Coupon increase + ad rank increase + review velocity increase = likely rank-push promotion.
- Large discount + weak sales response = clearance or failed promotion.
- BSR jump without ad keyword expansion = possible offsite or deal traffic.

Always infer promotion intent:

- rank push
- inventory clearance
- defense against competitor
- price elasticity test
- event-driven sale
- declining-link maintenance

## Advertising Strategy Signals

- Strong ad rank with weak natural rank: paid growth or launch push.
- Strong natural rank with lower ad rank: mature keyword asset or profit-control phase.
- High PPC bid and many ad competitors: expensive battlefield.
- Ads concentrated on large keywords: aggressive volume grab.
- Ads concentrated on long-tail keywords: efficiency and ACOS control.
- Brand terms and ASIN relation traffic: defensive posture.
- Competitor ASIN relations: offensive competitor interception.

Never infer exact spend, ACOS, TACOS, budget, or search term report details unless provided.

## Offsite Signals

Offsite is probabilistic. Use multiple signals:

- BSR jump without matching Amazon ad or keyword improvement.
- Review velocity acceleration not explained by sales/ad signals.
- Google Trends rising faster than Amazon keyword trend.
- Google, TikTok, YouTube, Reddit, influencer, coupon/deal site evidence.
- Review text mentions TikTok, influencer, video, blog, social media, coupon site, or recommendation.

Confidence guidance:

- High: Amazon trend anomaly plus direct offsite evidence.
- Medium: multiple internal anomalies but limited external evidence.
- Low: only one weak anomaly.

## Profit Pressure Signals

- Frequent couponing and declining price.
- Rising ad rank pressure in expensive keywords.
- Falling revenue despite stable or rising units.
- Heavy FBA or oversized item indicators.
- Low price band with high review moat and many sellers.

Do not claim exact margin unless COGS, FBA, referral fee, and ad cost are provided.

## Listing And Operator Profile

Infer operator type from pattern clusters:

- Factory type: many SKUs, low price, broad variants, weaker branding, supply-chain advantage.
- Boutique type: fewer SKUs, high image quality, precise positioning, stronger listing craft.
- Brand type: strong video/A+, external presence, branded search, consistent visual identity.
- Volume seller: many similar links, short lifecycle, frequent promotional cycling.
- Capital-backed push: fast scale, heavy ad/promotion, strong creative, aggressive category entry.

Treat this as a hypothesis and include counter-evidence.
