# QuickAdd AI Review

This provider-neutral recipe adds an AI-assisted review action to Obsidian. It creates a draft for review; it does not silently edit an existing contact.

Create a QuickAdd macro named `People: AI Contact Review` and configure it to:

1. Capture the active note or selected text.
2. Send it to your chosen AI plugin or command.
3. Use the “Create a Contact Note” prompt in `AI Workflows.md`.
4. Save the returned draft as a new note in `contacts/`.
5. Set `status: "review"` and `profile_complete: false`.
6. Open the new note for human review.

If the plugin cannot safely save a new file, have it return Markdown only and paste the result into a new note manually.

## Review Checklist

- Confirm the person's name and contact details.
- Remove anything inferred or unnecessary.
- Confirm the relationship type and tier.
- Add `first_met` only when known.
- Leave `next_contact_due` blank unless a follow-up is appropriate.
- Change `status` to `active` only after review.
