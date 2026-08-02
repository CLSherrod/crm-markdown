---
name: crm-markdown
description: Work with this local Markdown CRM to create, review, update, and organize human relationships, contact notes, tasks, follow-ups, companies, and AI-assisted drafts. Use when the user asks to manage contacts, extract relationship actions, prepare follow-ups, request missing contact information, or review CRM data in this repository.
---

# CRM Markdown Skill

Use this skill to help maintain the repository's Markdown CRM. Keep the system human-first: AI may organize information and draft language, but it must not invent facts, create pressure, or activate unreviewed records.

## Repository Map

- Real contacts: `contacts/`
- Sample contacts: `samples/`
- Company notes: `templates/Company Template.md` and company notes created from it
- AI workflows: `AI Workflows.md`
- AI review recipe: `QuickAdd AI Review.md`
- Contact schema: `templates/Contact Template.md`
- Dashboards: `Contacts.base` and `Follow-Up Dashboard.base`
- Reviews: `reviews/` using the monthly or weekly templates
- Validator: `scripts/validate_contacts.py`

Read the relevant reference before acting:

- Contact creation or update: `references/contact-schema.md`
- AI drafts, tasks, or information requests: `references/ai-workflows.md`
- Follow-up, review, or message work: `references/relationship-workflows.md`

## Non-Negotiable Rules

1. Never invent names, contact details, dates, relationship history, outcomes, deadlines, or consent.
2. Preserve unknowns as blank or `not-recorded`; list them under a review/confirmation section.
3. Treat AI-generated and imported records as `status: "review"` and `profile_complete: false`.
4. Do not change `review` to `active` without explicit human review or instruction.
5. Do not add real contact data to `samples/`.
6. Respect `do_not_contact: true`; do not propose routine outreach unless the user explicitly overrides it.
7. Preserve unaffected copy and history when updating a note.
8. Do not expose private contact information in generated examples, commits, or messages.

## Core Workflows

### Create a contact

1. Gather only the supplied source material.
2. Redact or minimize sensitive details when possible.
3. Draft frontmatter using the contact schema.
4. Set `status: "review"` for AI or imported records.
5. List missing or uncertain fields.
6. Save to `contacts/` only when the user asks to create the file.
7. Run the validator after file changes.

### Update a contact

1. Read the current note first.
2. Identify only fields supported by the new interaction.
3. Preserve all unrelated text and existing communication history.
4. Add a dated communication-log entry when an interaction occurred.
5. Update `last_contacted` only for a meaningful interaction.
6. Set `next_contact_due` only when a reminder is appropriate.
7. Show ambiguous changes for confirmation rather than silently applying them.

### Extract to-dos

Separate:

- the user's concrete actions;
- the other person's actions;
- possible actions that need confirmation.

Do not invent deadlines. Add confirmed actions under `## Open Tasks`. Use `next_contact_due` for a relationship reminder, not as a substitute for a concrete task.

### Draft outreach

Use the person's actual context, preferred method, and relationship tier. Keep requests easy to answer. Avoid generic urgency, artificial scarcity, manipulative sales language, or claims not present in the source notes.

### Review CRM health

Use the Bases views and validator to find:

- review/inbox records;
- duplicate names;
- missing contact reasons or meaningful topics;
- missing next steps;
- overdue follow-ups;
- inactive or archived records;
- opted-out contacts that must remain excluded.

## File Change Protocol

Before writing:

1. Check the repository status.
2. Read the exact target files.
3. Make the smallest coherent change.
4. Preserve unrelated worktree changes.

After writing:

1. Run `python3 scripts/validate_contacts.py`.
2. Run `python3 scripts/test_validate_contacts.py`.
3. Run `git diff --check`.
4. Report what changed and any items left for human review.

Never commit, publish, send messages, or contact people unless the user explicitly requests that separate action.
