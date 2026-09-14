#!/usr/bin/env python3
"""Build a fast, generated JSON index from canonical Markdown contact files."""
from pathlib import Path
import datetime as dt
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CONTACTS = ROOT / "contacts"
OUTPUT = ROOT / "generated" / "state.json"


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    values = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values


def date_or_none(value):
    try:
        return dt.date.fromisoformat(value) if value else None
    except ValueError:
        return None


def main():
    today = dt.date.today()
    contacts = []
    for path in sorted(CONTACTS.glob("*.md")):
        if path.name == "README.md":
            continue
        data = parse_frontmatter(path)
        due = date_or_none(data.get("next_contact_due", ""))
        last = date_or_none(data.get("last_contacted", ""))
        record = {
            "id": path.stem,
            "path": str(path.relative_to(ROOT)),
            "name": data.get("name", ""),
            "company": data.get("company", ""),
            "company_id": data.get("company_id", ""),
            "relationship_type": data.get("relationship_type", ""),
            "relationship_tier": data.get("relationship_tier", ""),
            "status": data.get("status", ""),
            "last_contacted": data.get("last_contacted", ""),
            "next_contact_due": data.get("next_contact_due", ""),
            "next_action": data.get("next_action", ""),
            "contact_reason": data.get("contact_reason", ""),
            "last_meaningful_topic": data.get("last_meaningful_topic", ""),
            "do_not_contact": data.get("do_not_contact", "false").lower() == "true",
            "days_since_contact": (today - last).days if last else None,
            "days_until_due": (due - today).days if due else None,
            "overdue": bool(due and due < today and data.get("do_not_contact", "false").lower() != "true"),
        }
        contacts.append(record)

    state = {
        "generated_on": today.isoformat(),
        "source": "contacts/*.md",
        "source_of_truth": "markdown",
        "contact_count": len(contacts),
        "contacts": contacts,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Built {OUTPUT.relative_to(ROOT)} with {len(contacts)} contacts.")


if __name__ == "__main__":
    main()
