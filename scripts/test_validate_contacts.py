#!/usr/bin/env python3
"""Small regression tests for validator assumptions."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_contacts import ALLOWED_STATUSES, DATE_FIELDS, REQUIRED  # noqa: E402
from validate_contacts import parse_frontmatter  # noqa: E402

assert {"inbox", "review", "active", "inactive", "archive"} == ALLOWED_STATUSES
assert "type" in REQUIRED and "next_contact_due" in REQUIRED
assert "last_contacted" in DATE_FIELDS
fixtures = ROOT / "scripts" / "fixtures"
assert parse_frontmatter(fixtures / "malformed.md") is None
assert parse_frontmatter(fixtures / "duplicate-a.md")["name"] == "Duplicate Example"
assert parse_frontmatter(fixtures / "duplicate-b.md")["name"] == "duplicate example"
print("Validator regression checks passed.")
