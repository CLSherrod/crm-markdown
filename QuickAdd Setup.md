# QuickAdd Setup

This guide sets up the three core QuickAdd actions for this vault:

1. `People: New Contact`
2. `People: Log Communication`
3. `People: Monthly Review`

Start with `Log Communication` and `Monthly Review`. Add `New Contact` after you are comfortable with the system.

## Recommended Hotkeys

Use these hotkeys:

```text
Cmd + Option + C  → People: New Contact
Cmd + Shift + L   → People: Log Communication
Cmd + Shift + M   → People: Monthly Review
```

For Windows/Linux, use:

```text
Ctrl + Alt + C    → People: New Contact
Ctrl + Shift + L  → People: Log Communication
Ctrl + Shift + M  → People: Monthly Review
```

Set hotkeys here:

```text
Settings → Hotkeys
```

Search for the QuickAdd command name, then assign the shortcut.

---

# People: New Contact

Use this to create a new person note inside the `contacts/` folder.

## Create the QuickAdd Choice

1. Open **Settings** in Obsidian.
2. Go to **Community plugins → QuickAdd → Manage Macros / Choices**.
3. Add a new choice.
4. Name it:

```text
People: New Contact
```

5. Set the choice type to:

```text
Template
```

## Template Settings

Use these settings:

```text
Template Path: templates/Contact Template.md
File Name Format: contacts/{{VALUE:Contact name}}
Create in folder: contacts
Append link: Disabled
Open: On
If file already exists: Keep existing file
```

If QuickAdd does not like the folder inside the file name, use this instead:

```text
File Name Format: {{VALUE:Contact name}}
Create in folder: contacts
```

## Recommended Command Palette Use

Run it from the command palette:

```text
QuickAdd: People: New Contact
```

Suggested hotkey:

```text
Cmd + Option + C
```

For Windows/Linux:

```text
Ctrl + Alt + C
```

## Rule

Real contact notes belong in:

```text
contacts/
```

Use simple filenames:

```text
First Last.md
```

Do not use long filenames like:

```text
First Last - Company - Client - Monthly.md
```

Keep filenames simple. Put the details inside the note properties.

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

Suggested hotkey:

```text
Cmd + Shift + L
```

For Windows/Linux:

```text
Ctrl + Shift + L
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

For Windows/Linux:

```text
Ctrl + Shift + M
```

## Monthly Rule

Create only one monthly review per month.

This is a relationship reset, not a productivity report. Keep it short and useful.
