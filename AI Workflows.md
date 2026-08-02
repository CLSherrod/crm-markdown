# AI Workflows

AI can make this CRM faster without turning relationships into an automated sales pipeline. Use it as a careful assistant: provide only the context you are comfortable sharing, ask it to preserve uncertainty, review its output, and save the final note yourself.

## Safety Rules

- Do not paste private contact information into an AI service unless you understand its privacy settings and have permission to do so.
- Replace names, email addresses, phone numbers, and company details with placeholders when possible.
- Ask AI to separate facts from guesses.
- Never let AI invent a birthday, address, relationship, deadline, outcome, or contact detail.
- Review every proposed change before adding it to a contact note.
- Use `not-recorded` or leave a field blank when information is unknown.

## Create a Contact Note

Give AI a conversation summary, meeting notes, email, or voice transcript and ask it to prepare a draft. Use this prompt:

```text
Create a draft contact note for this Markdown CRM.

Rules:
- Use the contact schema below.
- Preserve facts exactly.
- Do not infer missing information.
- Leave unknown fields blank.
- Use status: "inbox" and profile_complete: false unless there is enough information for a complete record.
- Suggest, but do not decide, relationship_type, relationship_tier, contact_cadence, and preferred_contact_method.
- Put uncertain items under "Needs confirmation".
- Do not create a follow-up date unless one was explicitly stated or clearly agreed.

Return:
1. A proposed YAML frontmatter block.
2. A short Snapshot section.
3. A Needs confirmation list.
4. A one-sentence explanation of the suggested tier and cadence.

Conversation or notes:
[PASTE REDACTED NOTES HERE]
```

After reviewing the result, save the note in `contacts/`, change `status` if appropriate, and add a deliberate `next_contact_due` date.

For AI-generated notes, use `status: "review"` first. Do not place an AI draft directly into an active follow-up view.

## Create To-Dos

Use AI to extract actions from a conversation without allowing it to create obligations that were never agreed:

```text
Extract possible to-dos from these notes.

Rules:
- Include only actions explicitly promised, requested, or clearly necessary.
- Separate my actions from the other person's actions.
- Preserve the original wording where possible.
- Do not invent deadlines.
- Mark unclear ownership or deadlines as "needs confirmation".
- Return concise Markdown checkboxes suitable for a contact note's ## Open Tasks section.

Notes:
[PASTE REDACTED NOTES HERE]
```

Add only confirmed actions to `## Open Tasks`. Use `next_contact_due` for a relationship reminder and an open task for a concrete action; do not use both for the same thing unless that is intentional.

## Ask for Missing Contact Information

AI can draft a respectful request when a contact record is incomplete:

```text
Draft a short, warm message asking this person for the missing contact information listed below.

Rules:
- Ask only for the information listed.
- Explain why it would be useful when appropriate.
- Do not sound like a form, sales pitch, or data-collection request.
- Offer an easy way to decline or share only what they prefer.
- Do not ask for sensitive information.
- Return email, text/WhatsApp, and in-person versions.

Person/context:
[PASTE MINIMAL CONTEXT HERE]

Missing information:
[EMAIL / PHONE / TIMEZONE / PREFERRED CONTACT METHOD / OTHER]
```

Once they respond, update only the fields they actually provided and record the date and method in the communication log.

## Turn a Conversation into a Complete Update

For an existing contact, ask AI for a proposed update rather than a rewritten note:

```text
Compare the current contact note with this new interaction.

Return only:
- fields that should change, with old value and proposed new value;
- a new communication-log entry;
- confirmed open tasks;
- unanswered questions.

Do not rewrite unaffected text. Do not invent dates, outcomes, or personal details.

Current note:
[PASTE REDACTED NOTE]

New interaction:
[PASTE REDACTED NOTES]
```

This keeps the contact history reviewable and prevents AI from quietly changing unrelated information.

## Running These Prompts in Obsidian

The prompts work with any AI tool that can accept selected Markdown or pasted text. A simple workflow is:

1. Open the source note or transcript.
2. Copy only the relevant, redacted section.
3. Run the appropriate prompt.
4. Paste the proposed result into a new note in `contacts/`.
5. Set `status: "review"` and inspect it before activating the record.

If using an Obsidian AI plugin, configure it to return text for review rather than automatically editing files. The repository does not require a particular provider or plugin.

## Communication-Quality Check

Before sending AI-assisted copy, ask:

- Is this message based on a real detail?
- Is the reason for contacting them clear?
- Is the request small and easy to answer?
- Does the tone fit the relationship and channel?
- Does it avoid pressure, urgency, or a hidden sales pitch?
- Have I removed claims or details AI invented?
