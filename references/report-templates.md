# Report Templates

## 中文导读

这些模板不是排版要求，而是为了强制每份报告保留推理痕迹。尤其要保留“第一性原理框架、证据账本、贝叶斯置信度更新、相变检查、时间最优行动、对抗性审查”。如果数据不足，也要显式写“数据不足导致置信度降低”，不要跳过。

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

1. Mode classification
- Why this mode:
- Analysis goal:

2. First-principles frame
- Decision target:
- Buyer job-to-be-done:
- Product reality:
- Inputs:
- Constraints:
- Minimum viable evidence:
- Dangerous assumptions:

3. Executive judgment
- Lifecycle:
- Threat level:
- Core advantage:
- Weakness:
- Recommended action:

4. Evidence ledger
- Observed facts:
- Inferences:
- Missing data:
- Source conflicts:

5. Bayesian confidence update
- Prior or baseline:
- Evidence raising confidence:
- Evidence lowering confidence:
- Updated confidence:

6. Phase-shift check
- Linear change or structural change:
- Signal:
- Alternative explanation:

7. Nine-layer analysis
- Product strategy:
- Market positioning:
- Keyword assets:
- Advertising posture:
- Listing conversion engineering:
- Review asset and pain points:
- Growth channels and offsite probability:
- Business model and profit pressure:
- Operator profile:

8. Promotion and price intelligence
- Detected or inferred promotions:
- Promotion intent:
- Evidence:
- Counter-evidence:

9. Time-optimal action
- Deep dive / monitor / counterattack / small test / ignore / stop:
- Why now:

10. How to compete
- Product:
- Listing:
- Pricing:
- Ads:
- Offsite:
- Follow-up watch points:

11. Red-team review
- What could be wrong:
- Strongest alternative explanation:
- What would disprove the conclusion:
```

## Batch Scan

```text
Mode: batch_scan
Marketplace:
Data sources:
ASIN count:
Data sufficiency:

1. Mode classification and first-principles frame
- Why batch scan:
- Decision target:
- Minimum viable evidence:

2. Market structure
- Price bands:
- Review moats:
- Brand/seller concentration:
- Lifecycle distribution:

3. Ranked competitor table
Columns:
ASIN | role | lifecycle | threat | growth signal | ad signal | promotion signal | review moat | confidence | next action

4. Abnormal signal watchlist
- Sudden growth:
- Heavy promotion:
- Ad aggression:
- Review acceleration:
- Possible offsite:

5. Bayesian and phase-shift summary
- Confidence changes:
- Structural shifts:
- Source conflicts:

6. Time-optimal action
- Which ASINs deserve time now:
- Which ASINs only need monitoring:

7. Recommended deep dives
- ASIN 1:
- ASIN 2:
- ASIN 3:

8. Red-team review
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
2. First-principles frame for comparison
3. Which ASIN deserves deep dive and why
4. Deep dive report for selected ASIN
5. What to monitor on the remaining ASINs
6. Red-team review
```

## Follow-Up Review

```text
Mode: follow_up_review
ASINs:
Previous snapshot:
Current snapshot:
Review window:

1. Mode classification and prior judgment
- Prior lifecycle:
- Prior threat level:
- Prior confidence:

2. Change summary
- Biggest positive changes:
- Biggest negative changes:
- No-change signals:

3. Bayesian update
- Prior judgment:
- New evidence:
- Updated confidence:
- What changed the view:

4. Phase-shift check
- Linear noise or structural change:
- Evidence:
- Alternative explanation:

5. Alert table
ASIN | change | possible cause | confidence | recommended action

6. Promotion and lifecycle updates
7. Time-optimal action
8. Next monitoring plan
9. Red-team review
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
