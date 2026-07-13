#!/usr/bin/env python3
"""Score competitor signals from normalized ASIN rows.

中文说明：
这个脚本只做启发式初筛，不做最终运营结论。
它根据销量增长、销售额增长、Review 增长、BSR 变化、Coupon、广告排名、
自然排名和流量占比，给增长、促销、广告、疑似站外打分。
最终报告仍必须结合 evidence-rules.md 做人工/Agent 复核。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def num(row: dict[str, Any], key: str, default: float = 0.0) -> float:
    """安全取数：字段不存在或无法转数字时返回默认值。"""
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
    """给单个 ASIN 行打启发式分数。

    注意：这些阈值是第一版默认值，适合用来发现异常，不适合当作绝对判断。
    后续可以按类目波动性调整，比如季节性强的类目需要提高增长阈值。
    """
    units_growth = num(row, "total_units_growth")
    revenue_growth = num(row, "total_amount_growth")
    review_growth = num(row, "reviews_increasement")
    bsr_cr = num(row, "bsr_rank_cr")
    coupon = num(row, "coupon")
    ad_position = num(row, "ad_position")
    natural_position = num(row, "rank_position")
    traffic_share = num(row, "traffic_percentage")

    # 增长分：销量/销售额/Review/BSR 同时变好时，说明链接可能处于起量或爆发。
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

    # 促销分：Coupon、降价换销量、Coupon 叠加 BSR 改善都说明促销驱动更强。
    promo_score = 0
    if coupon > 0:
        promo_score += 35
    if units_growth > 20 and revenue_growth < units_growth:
        promo_score += 25
    if bsr_cr > 20 and coupon > 0:
        promo_score += 25

    # 广告分：广告排名强于自然排名，通常说明 paid growth 或 launch push。
    ad_score = 0
    if ad_position and (not natural_position or ad_position < natural_position):
        ad_score += 35
    if ad_position and ad_position <= 20:
        ad_score += 25
    if traffic_share > 5:
        ad_score += 15

    # 疑似站外分：增长很强但广告信号不强时，才提高站外怀疑度。
    # 这只能提示“值得查站外证据”，不能直接认定投了站外。
    offsite_score = 0
    if growth_score >= 45 and ad_score < 25:
        offsite_score += 35
    if review_growth > 20 and ad_score < 25:
        offsite_score += 20
    if bsr_cr > 30 and coupon == 0 and ad_score < 25:
        offsite_score += 20

    # 生命周期假设：这里给的是粗分类，最终还要结合历史趋势和报告中的反证。
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
