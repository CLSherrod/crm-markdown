#!/usr/bin/env python3
"""Create a sanitized copy of Markdown before sharing it with an AI tool."""
from pathlib import Path
import argparse
import re

EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\w)(?:\+?\d[\d ()().-]{7,}\d)(?!\w)")
URL = re.compile(r"https?://[^\s)]+", re.I)

def redact(text):
    text = EMAIL.sub("[EMAIL REDACTED]", text)
    text = PHONE.sub("[PHONE REDACTED]", text)
    return URL.sub("[URL REDACTED]", text)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path)
parser.add_argument("destination", type=Path)
args = parser.parse_args()
if args.source.resolve() == args.destination.resolve():
    raise SystemExit("Refusing to overwrite the source file.")
args.destination.parent.mkdir(parents=True, exist_ok=True)
args.destination.write_text(redact(args.source.read_text(encoding="utf-8")), encoding="utf-8")
print(f"Wrote sanitized copy to {args.destination}")
