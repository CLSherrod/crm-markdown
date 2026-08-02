# Agent Profiles

`agents/openai.yaml` is metadata for the OpenAI/Codex skill interface.

`agents/ai-agents.yaml` is a provider-neutral registry for other AI tools. It points to short instruction files for Claude, Gemini, and local/open-source models.

Copy the relevant instruction file into the tool's project, system-prompt, or knowledge configuration. Keep `skills/crm-markdown/SKILL.md` as the canonical source when updating the workflow.

For setup steps by provider, see `Provider Installation.md` in the repository root.
