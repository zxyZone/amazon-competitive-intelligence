#!/usr/bin/env python3
"""Compare previous and current normalized ASIN snapshots.

中文说明：
这个脚本用于 follow_up_review 模式，对比上次快照和本次快照。
它只计算字段变化，不解释原因；原因解释应交给 Skill 的证据规则和金刚推理流程。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


# 跟进复盘重点字段。后续如果新增库存、Buy Box、Deal 标识、站外证据分数，
# 可以把字段加到这里，快照对比会自动输出变化。
WATCH_FIELDS = [
    "price",
    "coupon",
    "effective_price",
    "reviews",
    "reviews_increasement",
    "total_units",
    "total_amount",
    "bsr",
    "rank_position",
    "ad_position",
    "traffic_percentage",
]


def by_asin(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """按 ASIN 建索引，方便前后快照一一对比。"""
    return {str(row.get("asin")): row for row in rows if row.get("asin")}


def delta(previous: Any, current: Any) -> dict[str, Any]:
    """计算数值变化；非数值字段只保留前后值。"""
    result = {"previous": previous, "current": current, "delta": None, "delta_pct": None}
    try:
        prev = float(previous)
        cur = float(current)
    except (TypeError, ValueError):
        return result
    result["delta"] = cur - prev
    if prev:
        result["delta_pct"] = (cur - prev) / abs(prev) * 100
    return result


def compare(previous_rows: list[dict[str, Any]], current_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """输出每个 ASIN 的新增、缺失或字段变化。"""
    previous = by_asin(previous_rows)
    current = by_asin(current_rows)
    output = []
    for asin in sorted(set(previous) | set(current)):
        item = {"asin": asin, "status": "changed", "changes": {}}
        if asin not in previous:
            item["status"] = "new"
        elif asin not in current:
            item["status"] = "missing"
        for field in WATCH_FIELDS:
            item["changes"][field] = delta(previous.get(asin, {}).get(field), current.get(asin, {}).get(field))
        output.append(item)
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("previous", type=Path)
    parser.add_argument("current", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("snapshot_comparison.json"))
    args = parser.parse_args()

    previous_rows = json.loads(args.previous.read_text(encoding="utf-8"))
    current_rows = json.loads(args.current.read_text(encoding="utf-8"))
    compared = compare(previous_rows, current_rows)
    args.output.write_text(json.dumps(compared, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote comparison for {len(compared)} ASINs to {args.output}")


if __name__ == "__main__":
    main()
