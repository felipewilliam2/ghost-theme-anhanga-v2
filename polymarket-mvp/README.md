# Polymarket MVP (Simulation-first)

Goal: build a **market-making strategy simulator** using Polymarket public APIs (Gamma + Data API), starting with **top 20 markets by liquidity** and a **30-day historical dump**.

This MVP is *simulation only* (no order placement).

## Data sources
- **Gamma Markets API** (market discovery + metadata): https://gamma-api.polymarket.com
- **Data API** (public trades/history): https://data-api.polymarket.com
- **CLOB API** (public orderbook/price): https://clob.polymarket.com

## Quickstart
```bash
cd /home/node/.openclaw/workspace/polymarket-mvp
python3 src/dump_markets.py --limit 500 --top 20
python3 src/dump_trades.py --days 30 --per-token-limit 50000
```

Notes:
- Data API enforces a **max `offset` ~ 3000** for historical trades per token. This means we may not get full 30 days for extremely active markets in one go; we will still collect enough data for an MVP simulator.

Outputs:
- `data/markets_top.json`
- `data/trades/*.jsonl`

## Next steps
- Build simulator: `src/simulate_mm.py`
- Reports: `reports/summary.md`
