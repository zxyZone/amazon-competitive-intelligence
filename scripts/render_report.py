#!/usr/bin/env python3
"""Render a simple local HTML report from JSON or Markdown-like text."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


STYLE = """
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 40px; color: #17202a; }
main { max-width: 1040px; margin: 0 auto; }
h1, h2, h3 { color: #102a43; }
pre, code { background: #f4f7fb; border-radius: 6px; }
pre { padding: 16px; overflow: auto; }
table { border-collapse: collapse; width: 100%; margin: 16px 0; }
th, td { border: 1px solid #d9e2ec; padding: 8px; text-align: left; vertical-align: top; }
th { background: #edf2f7; }
.meta { color: #52616b; }
"""


def render_payload(text: str) -> str:
    try:
        data = json.loads(text)
        body = f"<pre>{html.escape(json.dumps(data, ensure_ascii=False, indent=2))}</pre>"
    except json.JSONDecodeError:
        escaped = html.escape(text)
        body = "<pre>" + escaped + "</pre>"
    return f"<!doctype html><html><head><meta charset='utf-8'><title>Amazon Competitive Intelligence</title><style>{STYLE}</style></head><body><main><h1>Amazon Competitive Intelligence</h1>{body}</main></body></html>"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("amazon_competitive_intelligence_report.html"))
    args = parser.parse_args()

    html_text = render_payload(args.input.read_text(encoding="utf-8"))
    args.output.write_text(html_text, encoding="utf-8")
    print(f"Wrote HTML report to {args.output}")


if __name__ == "__main__":
    main()
