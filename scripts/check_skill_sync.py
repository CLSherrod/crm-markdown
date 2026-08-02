#!/usr/bin/env python3
"""Check that the repository skill has required metadata and references."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
skill = root / "skills" / "crm-markdown"
required = [
    skill / "SKILL.md",
    skill / "agents" / "openai.yaml",
    skill / "references" / "contact-schema.md",
    skill / "references" / "ai-workflows.md",
    skill / "references" / "relationship-workflows.md",
    skill / "evals" / "cases.yaml",
    root / "agents" / "ai-agents.yaml",
    root / "agents" / "claude.md",
    root / "agents" / "gemini.md",
    root / "agents" / "local.md",
    root / "agents" / "claude-project.md",
    root / "agents" / "gemini-gem.md",
    root / "agents" / "ollama-modelfile.txt",
    root / "agents" / "open-webui.md",
    root / "agents" / "capability-matrix.yaml",
]
missing = [str(path.relative_to(root)) for path in required if not path.exists()]
text = (skill / "SKILL.md").read_text(encoding="utf-8")
for reference in ("contact-schema.md", "ai-workflows.md", "relationship-workflows.md"):
    if reference not in text:
        missing.append(f"SKILL.md reference: {reference}")
if missing:
    raise SystemExit("Skill check failed:\n- " + "\n- ".join(missing))
print("CRM skill structure and references are synchronized.")
