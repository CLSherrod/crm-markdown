# AI Contact Demo

```mermaid
flowchart LR
    A[Conversation or transcript] --> B[Redact private details]
    B --> C[AI creates proposed note]
    C --> D[Save with status review]
    D --> E[Human checks facts and consent]
    E --> F[Set status active]
    F --> G[Choose next contact date]
    G --> H[Log the interaction]
    H --> I[Review dashboard]
```

## Example

> Met Alex at a creative meetup. Alex runs a small video studio and wants to improve the studio website this autumn. We exchanged email addresses. No follow-up date was agreed.

AI should propose a record with `status: "review"`, `profile_complete: false`, a warm collaborator relationship, and no invented date. Confirm the full name, email, and meeting date before changing the record to `active`.

The AI proposes structure; it does not decide what belongs in the relationship record.
