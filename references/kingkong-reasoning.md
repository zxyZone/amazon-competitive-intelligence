# King Kong Reasoning

## 中文导读

本文件把“五大金刚/七段链路”落成竞品分析的强制推理顺序。使用时不要只在最后写一句“已审查”，而要让报告能看见每一步如何影响结论：为什么选这个模式、底层问题是什么、证据如何改变置信度、是否出现相变、现在最划算的行动是什么、反方如何推翻本结论。

Apply this as an explicit reasoning checklist, not as decorative labels.

## Mandatory Sequence

Use this sequence for every serious report:

1. Router: classify the task and explain why.
2. First principles: reduce the task to decision target, product/customer reality, available evidence, constraints, and minimum viable evidence.
3. Evidence ledger: separate observed facts, inferences, missing data, and conflicts.
4. Bounded Bayesian judgment: update confidence from incomplete evidence; never claim certainty.
5. Phase-shift detection: test whether trend changes are linear noise or structural changes.
6. Time-optimal action: choose the action that maximizes useful learning or commercial payoff per unit time.
7. Red-team review: attack the final judgment and list disconfirming evidence.

## Mode Mapping

- Router: classify the task as `single_deep_dive`, `batch_scan`, `compare_then_deep_dive`, or `follow_up_review`.
- First principles: define decision target, product/customer reality, inputs, outputs, constraints, and minimum viable evidence.
- Bounded Bayesian judgment: update confidence from incomplete evidence.
- Phase-shift detection: identify non-linear changes such as sudden BSR jumps, review acceleration, ad posture changes, or promotion shocks.
- Time-optimal action: choose monitor, deep dive, small test, counterattack, or ignore.
- Red-team review: attack the conclusion before finalizing.

## First-Principles Frame

Always answer:

- What decision are we helping the operator make?
- What job is the product doing for the buyer?
- What observable facts exist before any interpretation?
- Which constraints matter: data limits, category seasonality, ad cost, price band, review moat, supply chain, compliance?
- What is the minimum evidence needed to make a useful decision now?
- Which assumptions are unnecessary or dangerous?

Output the frame before the nine-layer analysis.

## Evidence Ledger

Use four buckets:

- Observed facts: tool output, file fields, screenshots, user-provided facts.
- Inferences: lifecycle, operator intent, ad posture, promotion intent, offsite probability.
- Missing data: fields or history that would materially change confidence.
- Conflicts: sources disagree or signals point in different directions.

Never mix these buckets.

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

## Time-Optimal Action

Choose one:

- Deep dive now: high threat, high learning value, or abnormal growth.
- Monitor: unclear but potentially important, needs another snapshot.
- Counterattack: competitor exposes a weakness we can act on now.
- Small test: uncertainty is high but test cost is low.
- Ignore: low threat, low learning value, or bad data quality.
- Stop: conclusion is too weak and more analysis is not worth the time.

Explain the time logic in one line.

## Red-Team Checklist

Before final output, check:

- Did we confuse correlation with causation?
- Did a promotion explain growth better than product-market pull?
- Did missing ad data cause overconfidence?
- Did a single review spike distort lifecycle judgment?
- Did category seasonality explain the trend?
- Did we ignore seller size, brand moat, variation structure, or price elasticity?
- Would the conclusion still hold if coupon or deal support ended?
