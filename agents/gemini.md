# Gemini CRM Instructions

Use `skills/crm-markdown/SKILL.md` as the governing instruction set for this repository, with `references/contact-schema.md` and `references/ai-workflows.md` as needed.

For every contact draft or import:

1. Preserve supplied facts exactly.
2. Leave unknown values blank or mark them for confirmation.
3. Use `status: "review"` and `profile_complete: false`.
4. Do not invent outreach dates, tasks, or consent.
5. Require human review before changing a record to `active`.

Respect `do_not_contact: true` and do not propose routine outreach for opted-out contacts.

For updates, propose only supported field changes and a communication-log entry. Do not rewrite unrelated contact history.
