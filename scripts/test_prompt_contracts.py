#!/usr/bin/env python3
"""Check that agent profiles retain the CRM safety contract."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = [root / "skills/crm-markdown/SKILL.md", *sorted((root / "agents").glob("*.md"))]
files = [path for path in files if path.name != "README.md"]
required = ("status", "review", "invent", "do_not_contact")
for path in files:
    text = path.read_text(encoding="utf-8")
    missing = [term for term in required if term not in text]
    if missing:
        raise SystemExit(f"{path}: missing safety terms: {', '.join(missing)}")
print(f"Checked {len(files)} CRM agent instruction files.")
