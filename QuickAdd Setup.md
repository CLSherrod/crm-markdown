# QuickAdd Setup

This guide sets up the three core QuickAdd actions for this vault:

1. `People: Log Communication`
2. `People: Monthly Review`
3. `People: New Contact`

Start with the first two. Add New Contact after you are comfortable with the system.

---

# People: Log Communication

Use this so you can add a communication log entry to a contact note in about 30 seconds.

## Goal

Open a contact note, run one command, answer a few prompts, and insert a clean log entry under `## Communication Log`.

## Create the QuickAdd Choice

1. Open **Settings** in Obsidian.
2. Go to **Community plugins → QuickAdd → Manage Macros / Choices**.
3. Add a new choice.
4. Name it:

```text
People: Log Communication
```

5. Set the choice type to:

```text
Capture
```

## Capture Settings

Use these settings:

```text
Capture to active file: On
Write position: After line
Insert after: ## Communication Log
Insert at end of section: On
Create line if not found: Off
Task: Off
Append link: Disabled
```

This assumes you are already inside the contact note when you run the command.

## Capture Format

Paste this into the Capture Format field:

```md

### {{DATE:YYYY-MM-DD}} — {{VALUE:Email,Text / WhatsApp,Phone call,Zoom call,In-person meeting,Commented on their post,Sent article/resource,Sent gift/card,Introduced them to someone,They contacted me|label:Method}}

- **Direction:** {{VALUE:Outbound,Inbound,Both|label:Direction}}
- **Summary:** {{VALUE:summary|type:multiline|label:What happened?}}
- **Next step:** {{VALUE:next_step|type:multiline|label:What is the next step?}}
- **Next contact due:** {{VDATE:next_contact_due,YYYY-MM-DD|next month}}
```

## After Logging

After the entry is inserted, manually update the contact properties at the top of the note:

```yaml
last_contacted: {{DATE:YYYY-MM-DD}}
next_contact_due: YYYY-MM-DD
contact_reason: ""
last_meaningful_topic: ""
```

Do not automate this yet. Manual updating keeps the system easier to understand and debug.

## Recommended Command Palette Use

Run it from the command palette:

```text
QuickAdd: People: Log Communication
```

Or assign a hotkey:

```text
Settings → Hotkeys → QuickAdd: People: Log Communication
```

Suggested hotkey:

```text
Cmd + Shift + L
```

## Rule

Only run this command while a real contact note is open.

Real contact notes belong in:

```text
contacts/
```

Sample contacts belong in:

```text
samples/
```

---

# People: Monthly Review

Use this once a month to create a fresh relationship review note from the monthly review template.

## Create the QuickAdd Choice

1. Open **Settings** in Obsidian.
2. Go to **Community plugins → QuickAdd → Manage Macros / Choices**.
3. Add a new choice.
4. Name it:

```text
People: Monthly Review
```

5. Set the choice type to:

```text
Template
```

## Template Settings

Use these settings:

```text
Template Path: templates/Monthly Review Template.md
File Name Format: reviews/{{DATE:YYYY-MM}} Monthly Relationship Review
Create in folder: reviews
Append link: Disabled
Open: On
If file already exists: Keep existing file
```

If QuickAdd does not like the folder inside the file name, use this instead:

```text
File Name Format: {{DATE:YYYY-MM}} Monthly Relationship Review
Create in folder: reviews
```

## Result

Running the command creates a note like:

```text
reviews/2026-06 Monthly Relationship Review.md
```

## Recommended Command Palette Use

Run it from the command palette:

```text
QuickAdd: People: Monthly Review
```

Suggested hotkey:

```text
Cmd + Shift + M
```

## Monthly Rule

Create only one monthly review per month.

This is a relationship reset, not a productivity report. Keep it short and useful.
