#!/usr/bin/env python3
"""Compare previous and current normalized ASIN snapshots."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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
    return {str(row.get("asin")): row for row in rows if row.get("asin")}


def delta(previous: Any, current: Any) -> dict[str, Any]:
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
