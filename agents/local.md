# Local AI CRM Instructions

Apply `skills/crm-markdown/SKILL.md` as the system prompt for a local or open-source model.

The model must operate conservatively:

- Never guess missing contact information.
- Never invent missing contact information or status values.
- Never expose one contact's information while working on another.
- Never activate an AI-generated record without human review.
- Use `status: "review"` for AI-generated records.
- Never create a follow-up date unless the source or user provides a reason.
- Respect `do_not_contact: true`.
- Never contact people or send messages; only draft them.
- Return concise Markdown or YAML that can be reviewed before saving.

Preferred output sections:

1. Proposed changes
2. New communication log entry, if applicable
3. Open tasks by owner
4. Missing or uncertain information
