#!/usr/bin/env python3
"""Score competitor signals from normalized ASIN rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def num(row: dict[str, Any], key: str, default: float = 0.0) -> float:
    value = row.get(key)
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).replace("%", "").replace(",", "").replace("$", ""))
    except ValueError:
        return default


def score_row(row: dict[str, Any]) -> dict[str, Any]:
    units_growth = num(row, "total_units_growth")
    revenue_growth = num(row, "total_amount_growth")
    review_growth = num(row, "reviews_increasement")
    bsr_cr = num(row, "bsr_rank_cr")
    coupon = num(row, "coupon")
    ad_position = num(row, "ad_position")
    natural_position = num(row, "rank_position")
    traffic_share = num(row, "traffic_percentage")

    growth_score = 0
    if units_growth > 30 or revenue_growth > 30:
        growth_score += 35
    elif units_growth > 10 or revenue_growth > 10:
        growth_score += 20
    if review_growth > 30:
        growth_score += 25
    elif review_growth > 10:
        growth_score += 10
    if bsr_cr > 30:
        growth_score += 20

    promo_score = 0
    if coupon > 0:
        promo_score += 35
    if units_growth > 20 and revenue_growth < units_growth:
        promo_score += 25
    if bsr_cr > 20 and coupon > 0:
        promo_score += 25

    ad_score = 0
    if ad_position and (not natural_position or ad_position < natural_position):
        ad_score += 35
    if ad_position and ad_position <= 20:
        ad_score += 25
    if traffic_share > 5:
        ad_score += 15

    offsite_score = 0
    if growth_score >= 45 and ad_score < 25:
        offsite_score += 35
    if review_growth > 20 and ad_score < 25:
        offsite_score += 20
    if bsr_cr > 30 and coupon == 0 and ad_score < 25:
        offsite_score += 20

    lifecycle = "unknown"
    if growth_score >= 60 and promo_score < 50:
        lifecycle = "breakout_or_ramp_up"
    elif growth_score >= 35:
        lifecycle = "ramp_up"
    elif promo_score >= 60 and growth_score < 35:
        lifecycle = "promotion_or_clearance"
    elif units_growth < -10 or revenue_growth < -10:
        lifecycle = "decline"
    elif row.get("reviews") and row.get("total_units"):
        lifecycle = "mature_or_stable"

    return {
        "asin": row.get("asin"),
        "title": row.get("title"),
        "scores": {
            "growth": min(growth_score, 100),
            "promotion": min(promo_score, 100),
            "advertising": min(ad_score, 100),
            "offsite_suspected": min(offsite_score, 100),
        },
        "lifecycle_hypothesis": lifecycle,
        "confidence_note": "Heuristic score from available normalized fields; inspect evidence before final judgment.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("competitor_signal_scores.json"))
    args = parser.parse_args()

    rows = json.loads(args.input.read_text(encoding="utf-8"))
    scored = [score_row(row) for row in rows]
    args.output.write_text(json.dumps(scored, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(scored)} scored rows to {args.output}")


if __name__ == "__main__":
    main()
