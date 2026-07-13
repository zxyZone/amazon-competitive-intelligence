---
name: amazon-competitive-intelligence
description: Amazon competitor intelligence workflow for SellerSprite, SIF, Sorftime MCP data or manual Amazon research imports. Use when analyzing one ASIN, scanning batches of competitor ASINs, reviewing follow-up changes, inferring competitor lifecycle, ads, promotions, offsite signals, pricing, reviews, listing strategy, or building evidence-backed next actions for Amazon operations.
---

# Amazon Competitive Intelligence

## 中文导读

这个 Skill 的目标不是简单生成一份竞品报告，而是把竞品 ASIN 当成一个运营系统来拆解：先判断任务模式，再确认数据边界，然后用金刚推理流程把事实、推断、置信度、反证和下一步动作分开输出。

核心使用原则：

- 先看输入属于单 ASIN 深潜、批量竞对扫描、对比后深潜，还是跟进复盘。
- 先用 SellerSprite、SIF、Sorftime MCP；没有 MCP 时再吃用户导入的表格、截图、链接、Keepa 导出。
- 所有结论必须区分“观察事实”和“运营推断”，不能把推测写成后台真相。
- 生成 HTML、写飞书、提交 GitHub、开启定时任务前都要先问用户确认。

## Overview

Use this skill to analyze Amazon competitors with evidence, confidence, counter-evidence, and next actions. Prefer connected MCP sources first, fall back to user-provided files, and label every conclusion as observed fact, inference, or unknown.

## Mode Router

Choose the mode in this order:

1. Use the mode explicitly requested by the user.
2. Infer from input shape.
3. Infer from intent keywords.
4. Default to batch scan, then recommend 3-5 ASINs for deep dives.

Modes:

- `single_deep_dive`: one ASIN, or requests such as "deep dive this ASIN", "analyze this competitor", "reverse engineer this listing".
- `batch_scan`: 6+ ASINs, category Top lists, SellerSprite/SIF/Sorftime exports, or requests such as "scan competitors", "find key rivals", "compare these ASINs".
- `follow_up_review`: requests containing "follow up", "review changes", "since last time", "weekly", "monitor", "alert", or two snapshots for comparison.
- `compare_then_deep_dive`: 2-5 ASINs. Rank them first, then deep dive the most important one unless the user specifies otherwise.

## Data Boundary

Only use these sources:

1. Connected MCP tools from SellerSprite, SIF, or Sorftime.
2. User-provided Excel, CSV, JSON, screenshots, links, copied Amazon page text, Keepa exports, or historical snapshots.
3. User-authorized web search or external lookup.

Do not assume private Seller Central data, competitor ad spend, TACOS, exact inventory, backend experiments, or exact offsite budget. Infer them only from signals and mark confidence.

For data requirements and fallback fields, read `references/data-sources.md`.

## Core Workflow

1. Identify mode and marketplace.
2. Inventory available data sources. Use MCP if available; otherwise request/import the minimum manual files.
3. Normalize evidence into ASIN-level facts: product, price, BSR/sales, review, keyword, ad, coupon/deal, listing, relation, and history fields.
4. Apply the King Kong reasoning sequence from `references/kingkong-reasoning.md`: classify, first-principles framing, bounded Bayesian update, phase-shift detection, time-optimal action, and red-team review.
5. Apply evidence rules from `references/evidence-rules.md`.
6. Produce the matching report template from `references/report-templates.md`.
7. End with next actions, missing data, and a red-team review.
8. Ask before creating persistent outputs such as HTML reports, Feishu records, GitHub commits, or scheduled tasks.

## Required Reasoning Blocks

Every full report must include these blocks, even if some are brief:

1. `Mode classification`: why this is single deep dive, batch scan, compare-then-deep-dive, or follow-up review.
2. `First-principles frame`: target decision, product/customer/job-to-be-done, inputs, outputs, constraints, and minimum viable evidence.
3. `Evidence ledger`: observed facts, inferred conclusions, missing data, source conflicts.
4. `Bayesian confidence update`: prior or baseline assumption, evidence that raises/lowers confidence, updated confidence.
5. `Phase-shift check`: whether growth, promotion, ads, reviews, price, or offsite signals show non-linear change.
6. `Time-optimal action`: deep dive, monitor, counterattack, small test, ignore, or stop.
7. `Red-team review`: strongest alternative explanation and what would disprove the recommendation.

## MCP Usage Guidance

When MCP tools are available, prefer this order:

1. ASIN detail and coupon/deal data.
2. Sales, BSR, price, and historical prediction data.
3. Traffic keywords, natural rank, ad rank, PPC bid, traffic share.
4. Related listings and competitor pool data.
5. Reviews and review filters.
6. Google Trends through supported MCP sources when evaluating external demand.

When multiple MCP sources are available, treat SellerSprite, SIF, and Sorftime as parallel evidence sources. Do not force reconciliation; report agreement, conflict, and confidence.

## Manual File Helpers

Use scripts only for deterministic file work:

- `scripts/normalize_sellersprite_export.py`: normalize CSV, JSON, or XLSX exports into canonical JSON.
- `scripts/score_competitor_signals.py`: score lifecycle, promotion, ad, and offsite signals from normalized data.
- `scripts/compare_snapshots.py`: compare two ASIN snapshots for follow-up review.
- `scripts/render_report.py`: render a confirmed JSON/Markdown report payload to local HTML.

These scripts are optional helpers. If a file format is messy, inspect it first and adapt carefully.

## Output Rules

Every important judgment must include:

- Evidence: fields, tool output, file rows, screenshots, or user-provided observations.
- Inference: the operational interpretation.
- Confidence: high, medium, or low.
- Counter-evidence: what could make the inference wrong.
- Next action: what to monitor, test, copy, avoid, or deep dive next.

Never present inferred data as fact. For example, say "likely promotion-driven growth" rather than "they spent heavily on ads" unless the data directly proves it.

## Follow-Up And Automation

Follow-up review can support scheduled reminders later, but do not create an automation by default. Read `references/follow-up-automation.md` when the user asks for scheduled monitoring, Feishu push, GitHub Actions cron, or recurring Codex reminders.
