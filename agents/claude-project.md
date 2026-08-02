# Claude Project Instructions

Use `skills/crm-markdown/SKILL.md` as the governing CRM workflow. Read the relevant files in `skills/crm-markdown/references/` before changing records.

Draft AI-created or imported contacts with `status: "review"` and `profile_complete: false`. Never invent contact details, dates, consent, or deadlines. Preserve unaffected history, respect `do_not_contact: true`, and ask for confirmation when ownership or facts are unclear.

For external processing, sanitize source notes first with:

```text
python3 scripts/redact_for_ai.py input.md sanitized/input.md
```

Return proposed changes for review before writing files.
