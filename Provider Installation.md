# Provider Installation

This guide installs the CRM instructions into common AI tools. The repository skill is provider-neutral, but each tool handles files and private data differently.

Before using any provider, read `Privacy .gitignore.example` and consider creating a sanitized copy with:

```text
python3 scripts/redact_for_ai.py input.md sanitized/input.md
```

AI-generated or imported contacts must remain `status: "review"` until you inspect them.

## OpenAI / Codex

The skill is already installed locally at:

```text
~/.codex/skills/crm-markdown/
```

For repository work, open this folder as the workspace and invoke `$crm-markdown`. The UI metadata is in `skills/crm-markdown/agents/openai.yaml`.

Recommended mode: repository-aware, review before writing.

## Claude Projects

1. Create or open a Claude Project.
2. Add the repository files as project knowledge, especially `skills/crm-markdown/SKILL.md`, `skills/crm-markdown/references/`, `AI Workflows.md`, and `templates/Contact Template.md`.
3. Paste the contents of `agents/claude-project.md` into the project instructions.
4. If Claude cannot access the local repository, paste sanitized source notes and copy approved Markdown back manually.

Recommended mode: draft-only unless a trusted file integration is explicitly enabled.

## Gemini Gems

1. Create a Gem for this CRM.
2. Add the repository skill and reference files as knowledge, or paste their relevant contents.
3. Use `agents/gemini-gem.md` as the Gem instructions.
4. Keep contact data out of Gemini unless the account and sharing settings are appropriate.

Recommended mode: draft-only with manual file updates.

## Ollama

1. Copy `agents/ollama-modelfile.txt` to a working Modelfile.
2. Replace `your-local-model` with the local model you want to use.
3. Build the model with your normal Ollama workflow.
4. Provide the CRM skill and references in the model's working context or system prompt.
5. Use the redaction script when notes will leave the local machine; with Ollama, keep processing local when possible.

Recommended mode: local, draft-only, human review before file changes.

## Open WebUI

1. Create a new model preset or workspace.
2. Use `agents/open-webui.md` as the system prompt.
3. Add `skills/crm-markdown/SKILL.md` and the relevant references as knowledge files.
4. Enable file tools only if you understand where writes occur.
5. Keep the default behavior draft-only and review proposed changes before saving.

Recommended mode: draft-only unless file tools are explicitly configured and trusted.

## Capability Differences

See `agents/capability-matrix.yaml`. A provider's ability to read or write files depends on its integration, not only on the model. Never assume that an AI can safely edit the repository merely because it can discuss its contents.
