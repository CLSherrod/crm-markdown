# Agent Operating Protocol

This CRM is Markdown-first. Human-readable Markdown records are the source of truth.

## Rules

1. Edit canonical records in `contacts/`, company records, and `opportunities/` only when the requested facts are known.
2. Never invent contact details, dates, relationship status, company links, or next actions.
3. Put imported or AI-created contacts in `status: review` until a human confirms them.
4. Never treat `generated/state.json` as canonical data and never hand-edit it.
5. After changing canonical CRM records, run `python3 scripts/validate_contacts.py` and then `python3 scripts/build_state.py`.
6. `contact_reason` answers why reaching out matters. `next_action` answers what should actually happen next.
7. Respect `do_not_contact: true`; do not create or advance follow-up reminders for that person.
8. Preserve communication history. Add entries rather than rewriting old interactions unless correcting a factual error.
9. Prefer stable `company_id` links over matching companies only by display name.
10. Keep the CRM human-scale. Do not add sales machinery unless it supports an actual relationship or opportunity.

## Generated State

`generated/state.json` is a disposable read-optimized index for agents and scripts. Rebuild it from Markdown whenever canonical records change.

## Activity Log

Agent automations may append newline-delimited JSON events to `logs/activity.jsonl`. This log is supplementary history, not the source of truth for contact facts.
