# Field Definitions

Use these fields consistently so the dashboards remain useful.

| Field | Meaning |
| --- | --- |
| `last_contacted` | The date of the latest meaningful interaction, inbound or outbound. |
| `next_contact_due` | The date you want a reminder, not a promise that contact must happen. |
| `contact_reason` | The specific reason to reach out next. |
| `last_meaningful_topic` | The most useful context to remember before writing. |
| `status: inbox` | A new or incomplete contact that is not ready for routine follow-up. |
| `status: review` | An AI-assisted or imported record waiting for human review. |
| `status: inactive` | A known relationship that is not currently active but should remain easy to find. |
| `do_not_contact: true` | Exclude the person from follow-up views until this is deliberately changed. |
| `status: archive` | No active relationship work; retain the note for history. |

If someone does not reply, record the attempt in the log and choose the next reminder deliberately. Do not keep moving the date indefinitely without a reason.

## Status Workflow

```text
inbox → review → active → inactive → archive
```

Use `review` for anything drafted by AI or imported from another system. Confirm the facts, remove guesses, set the relationship fields, and only then change it to `active`.
