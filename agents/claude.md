# Claude CRM Instructions

You are working with the CRM Markdown skill in `skills/crm-markdown/SKILL.md`.

Read that file and the relevant references before changing CRM files. Follow these rules:

- Never invent contact facts, dates, deadlines, consent, or relationship history.
- Treat AI-created or imported contacts as `status: "review"` and `profile_complete: false`.
- Preserve unaffected text and existing communication history.
- Respect `do_not_contact: true`.
- Keep private contact information out of examples and public output.
- Run the repository validation commands after changes.

When the user provides notes, first return a proposed change or draft unless they explicitly ask you to write files. Ask for confirmation when facts or ownership are ambiguous.
