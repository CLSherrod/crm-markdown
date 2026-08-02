#!/usr/bin/env python3
"""Validate contact frontmatter without modifying the vault."""
from pathlib import Path
import datetime as dt
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTACTS = ROOT / "contacts"
SAMPLES = ROOT / "samples"
REQUIRED = {"type", "name", "status", "relationship_tier", "last_contacted", "next_contact_due", "do_not_contact"}
ALLOWED_STATUSES = {"inbox", "review", "active", "inactive", "archive"}
DATE_FIELDS = {"first_met", "last_contacted", "next_contact_due", "birthday"}

def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    values = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values

errors = []
paths = [path for path in sorted(CONTACTS.glob("*.md")) if path.name != "README.md"]
sample_paths = sorted(SAMPLES.glob("*.md"))
all_paths = paths + sample_paths
names = {}
for path in all_paths:
    data = parse_frontmatter(path)
    if data is None:
        errors.append(f"{path.name}: missing or malformed frontmatter")
        continue
    missing = REQUIRED - data.keys()
    if missing:
        errors.append(f"{path.name}: missing {', '.join(sorted(missing))}")
    if data.get("type") != "contact":
        errors.append(f"{path.name}: type must be contact")
    if data.get("status") not in ALLOWED_STATUSES:
        errors.append(f"{path.name}: unknown status {data.get('status')!r}")
    name = data.get("name", "").strip().casefold()
    if name:
        names.setdefault(name, []).append(path.name)
    for field in DATE_FIELDS:
        value = data.get(field, "")
        if value and value not in {"YYYY-MM-DD", ""}:
            try:
                dt.date.fromisoformat(value)
            except ValueError:
                errors.append(f"{path.name}: {field} is not YYYY-MM-DD")
    if data.get("status") == "archive" and not data.get("archive_reason"):
        errors.append(f"{path.name}: archived contact needs archive_reason")
    if data.get("do_not_contact") == "true" and data.get("next_contact_due"):
        errors.append(f"{path.name}: do_not_contact contact should not have next_contact_due")

for name, files in names.items():
    if len(files) > 1:
        errors.append(f"duplicate contact name {name!r}: {', '.join(files)}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Validated {len(paths)} real contact notes and {len(sample_paths)} sample notes successfully.")
