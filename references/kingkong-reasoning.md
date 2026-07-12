# King Kong Reasoning

Apply this as an explicit reasoning checklist, not as decorative labels.

## Mode Mapping

- Router: classify the task as `single_deep_dive`, `batch_scan`, `compare_then_deep_dive`, or `follow_up_review`.
- First principles: define decision target, inputs, outputs, constraints, and minimum viable evidence.
- Bounded Bayesian judgment: update confidence from incomplete evidence.
- Phase-shift detection: identify non-linear changes such as sudden BSR jumps, review acceleration, ad posture changes, or promotion shocks.
- Time-optimal action: choose monitor, deep dive, small test, counterattack, or ignore.
- Red-team review: attack the conclusion before finalizing.

## Single ASIN Deep Dive

Use:

1. First principles to describe what this link sells, who buys it, and why the operator chose this structure.
2. Bounded Bayesian judgment to infer lifecycle, ad strategy, promotion intent, offsite probability, and profit pressure.
3. Phase-shift detection to identify growth, decline, listing refresh, deal-driven bursts, or channel changes.
4. Red-team review to prevent overfitting one ASIN.

## Batch Scan

Use:

1. Router to rank ASINs by strategic importance.
2. Bounded Bayesian judgment to score opportunity, threat, abnormal growth, ad intensity, and review moat.
3. Time-optimal action to decide which ASINs deserve deep dive now.
4. Red-team review to catch sampling bias from Top lists or temporary promotions.

## Follow-Up Review

Use Bayesian updating:

- Start with the prior judgment from the last report.
- Add current evidence.
- Update confidence up or down.
- Explain what changed and what did not.

Example:

```text
Prior: likely offsite-assisted growth, confidence 60%.
New evidence: BSR improved again, review velocity rose, ad keyword coverage stayed weak.
Updated judgment: offsite-assisted growth confidence 75%.
Counter-evidence: could also be a short Amazon Deal event.
```

## Red-Team Checklist

Before final output, check:

- Did we confuse correlation with causation?
- Did a promotion explain growth better than product-market pull?
- Did missing ad data cause overconfidence?
- Did a single review spike distort lifecycle judgment?
- Did category seasonality explain the trend?
- Did we ignore seller size, brand moat, variation structure, or price elasticity?
- Would the conclusion still hold if coupon or deal support ended?
