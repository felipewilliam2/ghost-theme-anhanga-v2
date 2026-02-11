#!/usr/bin/env python3

"""Dump active Polymarket markets and select top-N by liquidity.

Writes:
- data/markets_raw.json
- data/markets_top.json
"""

import argparse
import json
import os
from datetime import datetime

from http_utils import get_json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

GAMMA = "https://gamma-api.polymarket.com"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=500, help="How many active markets to fetch from Gamma")
    ap.add_argument("--top", type=int, default=20, help="How many markets to keep (by liquidityNum)")
    args = ap.parse_args()

    markets = get_json(
        f"{GAMMA}/markets",
        {
            "active": "true",
            "closed": "false",
            "limit": args.limit,
        },
    )

    os.makedirs(DATA_DIR, exist_ok=True)

    with open(os.path.join(DATA_DIR, "markets_raw.json"), "w", encoding="utf-8") as f:
        json.dump(markets, f, ensure_ascii=False, indent=2)

    def liq(m):
        # Gamma returns both string and numeric versions
        return float(m.get("liquidityNum") or m.get("liquidity") or 0.0)

    top = sorted(markets, key=liq, reverse=True)[: args.top]

    payload = {
        "generatedAtUtc": datetime.utcnow().isoformat() + "Z",
        "source": "gamma-api.polymarket.com/markets?active=true&closed=false",
        "topBy": "liquidityNum",
        "top": args.top,
        "markets": top,
    }

    with open(os.path.join(DATA_DIR, "markets_top.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Fetched {len(markets)} markets; wrote top {len(top)} → {os.path.join(DATA_DIR, 'markets_top.json')}")


if __name__ == "__main__":
    main()
