#!/usr/bin/env python3
"""Create an Obsidian daily note from the existing template.

- Target vault: /home/node/.openclaw/workspace/obsidian-vault
- Template: 99_System/Templates/Tpl_Daily_Note_Automatico.md
- Output: 05_Daily/YYYY-MM-DD.md

This is intentionally simple (no Obsidian plugins required).
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path("/home/node/.openclaw/workspace/obsidian-vault")
TEMPLATE = VAULT / "99_System" / "Templates" / "Tpl_Daily_Note_Automatico.md"
DAILY_DIR = VAULT / "05_Daily"


def render_template(raw: str, date: datetime) -> str:
    # Minimal replacement for templater placeholders used in this template.
    # We keep unknown placeholders intact.
    yyyy_mm_dd = date.strftime("%Y-%m-%d")
    dd_mm_yyyy = date.strftime("%d/%m/%Y")
    weekday_en = date.strftime("%A")

    out = raw
    out = out.replace('<% tp.date.now("YYYY-MM-DD") %>', yyyy_mm_dd)
    out = out.replace('<% tp.date.now("DD/MM/YYYY") %>', dd_mm_yyyy)
    out = out.replace('<% tp.date.now("dddd") %>', weekday_en)
    # Template has a small typo/missing % in one line; we normalize it too.
    out = out.replace('<% tp.date.now("dddd") %', weekday_en)

    # Replace {{date:HH:mm}} with current UTC time for reproducibility.
    out = out.replace("{{date:HH:mm}}", datetime.now(timezone.utc).strftime("%H:%M"))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (defaults to today UTC)")
    ap.add_argument("--force", action="store_true", help="overwrite if exists")
    args = ap.parse_args()

    if args.date:
        date = datetime.strptime(args.date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    else:
        date = datetime.now(timezone.utc)

    DAILY_DIR.mkdir(parents=True, exist_ok=True)

    out_path = DAILY_DIR / f"{date.strftime('%Y-%m-%d')}.md"
    if out_path.exists() and not args.force:
        print(f"exists: {out_path}")
        return

    raw = TEMPLATE.read_text(encoding="utf-8")
    content = render_template(raw, date)
    out_path.write_text(content, encoding="utf-8")
    print(f"wrote: {out_path}")


if __name__ == "__main__":
    main()
