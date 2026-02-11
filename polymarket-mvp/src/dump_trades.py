#!/usr/bin/env python3

"""Dump recent trades for each token in `data/markets_top.json` using Data API.

Uses: https://data-api.polymarket.com/trades?token_id=...&limit=...&offset=...

Writes: data/trades/{marketId}_{tokenId}.jsonl
"""

import argparse
import json
import os
import time
from datetime import datetime, timedelta, timezone

from http_utils import get_json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

DATA_API = "https://data-api.polymarket.com"


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--page", type=int, default=500, help="page size for data-api trades")
    ap.add_argument("--per-token-limit", type=int, default=100000, help="safety cap")
    ap.add_argument("--sleep", type=float, default=0.15, help="sleep between requests")
    ap.add_argument("--max-markets", type=int, default=None, help="debug: only process first N markets")
    args = ap.parse_args()

    with open(os.path.join(DATA_DIR, "markets_top.json"), "r", encoding="utf-8") as f:
        top = json.load(f)["markets"]

    if args.max_markets is not None:
        top = top[: args.max_markets]

    cutoff = int((utc_now() - timedelta(days=args.days)).timestamp())
    trades_dir = os.path.join(DATA_DIR, "trades")
    os.makedirs(trades_dir, exist_ok=True)

    total_files = 0
    for m in top:
        market_id = m.get("id")
        token_ids = json.loads(m.get("clobTokenIds"))

        for token_id in token_ids:
            out_path = os.path.join(trades_dir, f"{market_id}_{token_id}.jsonl")
            n = 0
            offset = 0
            min_ts = None

            with open(out_path, "w", encoding="utf-8") as out:
                while True:
                    if n >= args.per_token_limit:
                        break

                    # Data API enforces a max historical activity offset (observed: 3000).
                    if offset > 3000:
                        break

                    batch = get_json(
                        f"{DATA_API}/trades",
                        {
                            "token_id": token_id,
                            "limit": args.page,
                            "offset": offset,
                        },
                        timeout=30,
                    )

                    if not batch:
                        break

                    for t in batch:
                        ts = int(t.get("timestamp"))
                        if min_ts is None or ts < min_ts:
                            min_ts = ts
                        if ts < cutoff:
                            # stop once we are older than cutoff
                            batch = []
                            break
                        out.write(json.dumps(t, ensure_ascii=False) + "\n")
                        n += 1

                    if not batch:
                        break

                    offset += len(batch)
                    time.sleep(args.sleep)

            total_files += 1
            print(f"wrote {out_path} trades={n} min_ts={min_ts} cutoff={cutoff}", flush=True)

    meta = {
        "generatedAtUtc": utc_now().isoformat(),
        "days": args.days,
        "cutoffEpoch": cutoff,
        "files": total_files,
    }
    with open(os.path.join(trades_dir, "_meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
