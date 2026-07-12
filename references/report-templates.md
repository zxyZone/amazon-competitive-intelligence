# Report Templates

## Table Of Contents

- Single ASIN Deep Dive
- Batch Scan
- Compare Then Deep Dive
- Follow-Up Review
- Short Alert Format

## Single ASIN Deep Dive

```text
Mode: single_deep_dive
ASIN:
Marketplace:
Data sources:
Data sufficiency:

1. Executive judgment
- Lifecycle:
- Threat level:
- Core advantage:
- Weakness:
- Recommended action:

2. Evidence table
- Observed facts:
- Inferences:
- Missing data:

3. Nine-layer analysis
- Product strategy:
- Market positioning:
- Keyword assets:
- Advertising posture:
- Listing conversion engineering:
- Review asset and pain points:
- Growth channels and offsite probability:
- Business model and profit pressure:
- Operator profile:

4. Promotion and price intelligence
- Detected or inferred promotions:
- Promotion intent:
- Evidence:
- Counter-evidence:

5. How to compete
- Product:
- Listing:
- Pricing:
- Ads:
- Offsite:
- Follow-up watch points:

6. Red-team review
- What could be wrong:
- What would disprove the conclusion:
```

## Batch Scan

```text
Mode: batch_scan
Marketplace:
Data sources:
ASIN count:
Data sufficiency:

1. Market structure
- Price bands:
- Review moats:
- Brand/seller concentration:
- Lifecycle distribution:

2. Ranked competitor table
Columns:
ASIN | role | lifecycle | threat | growth signal | ad signal | promotion signal | review moat | confidence | next action

3. Abnormal signal watchlist
- Sudden growth:
- Heavy promotion:
- Ad aggression:
- Review acceleration:
- Possible offsite:

4. Recommended deep dives
- ASIN 1:
- ASIN 2:
- ASIN 3:

5. Red-team review
- Sampling bias:
- Missing data:
- Temporary-promotion risk:
```

## Compare Then Deep Dive

```text
Mode: compare_then_deep_dive
ASINs:
Marketplace:

1. Quick comparison
2. Which ASIN deserves deep dive and why
3. Deep dive report for selected ASIN
4. What to monitor on the remaining ASINs
```

## Follow-Up Review

```text
Mode: follow_up_review
ASINs:
Previous snapshot:
Current snapshot:
Review window:

1. Change summary
- Biggest positive changes:
- Biggest negative changes:
- No-change signals:

2. Bayesian update
- Prior judgment:
- New evidence:
- Updated confidence:
- What changed the view:

3. Alert table
ASIN | change | possible cause | confidence | recommended action

4. Promotion and lifecycle updates
5. Next monitoring plan
6. Red-team review
```

## Short Alert Format

```text
Competitor alert:
ASIN:
Change:
Likely cause:
Confidence:
Evidence:
Counter-evidence:
Action:
Needs deep dive: yes/no
```
