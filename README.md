# CRM in Markdown

A simple, local-first networking and lightweight CRM system built entirely with Markdown files.

No subscriptions. No lock-in. No bloated sales pipeline. Just plain text you control.

This project is designed for people who want to remember people, follow up with care, share useful knowledge, make thoughtful introductions, and keep a useful communication history without handing their relationship data to another SaaS platform.

## What This Is

**CRM in Markdown** is a Markdown-first, Obsidian-enhanced networking system.

It helps you track and nurture relationships with:

- Friends
- Collaborators
- Clients
- Leads
- Mentors
- Community relationships

The system is intentionally simple: **one person = one contact note**.

Each contact note includes the person’s profile, relationship type, relationship tier, follow-up rhythm, next contact date, and communication log.

## What This Is Not

This is not a heavy sales CRM.

It does not try to replace Salesforce, HubSpot, or a full business automation platform. It is a calm, human-scale system for staying in touch with people who matter.

This is also not a cold outreach machine. The goal is not to squeeze value from relationships. The goal is to remember people, help where you can, and stay connected in a thoughtful way.

## Core Philosophy

Most networking systems fail because they become another job.

This system is built around a 30-second habit:

1. Open the person’s contact note.
2. Add a short communication log entry.
3. Update `last_contacted`.
4. Update `next_contact_due`.
5. Move on.

Consistency matters more than complexity.

## Five-Minute Quick Start

1. Open this folder as an Obsidian vault.
2. Enable the Bases core plugin and install QuickAdd if you want shortcuts.
3. Open `samples/` and copy one example to `contacts/` to learn the format.
4. Create a real contact in `contacts/` using `templates/Contact Template.md`.
5. Log one interaction, update the reminder fields, and open `Follow-Up Dashboard.base`.

Keep new or incomplete records at `status: "inbox"` until you have enough context to follow up thoughtfully.

The best networking is generous: share useful resources, make good introductions, say thank you, and follow up when it actually matters.

## Features

- **One Markdown file per person**
- **One communication log per person**
- **Monthly, quarterly, yearly, and custom follow-up cadences**
- **Manual next-contact dates for real flexibility**
- **Obsidian Bases dashboards for reminders**
- **Contact Today, Overdue, and This Week views**
- **Relationship tiers so not everyone gets the same attention**
- **Personal and business fields**
- **QuickAdd setup guide for fast contact creation, communication logging, and monthly reviews**
- **Reusable value-first networking message templates**
- **Optional AI workflows for drafting contacts, extracting to-dos, and requesting missing contact information**
- **Templates for contacts, companies, communication logs, and monthly reviews**
- **Example data you can delete or adapt**
- **A local validation script for note properties and reminder safety**

## Privacy and Backups

Contact notes can contain sensitive personal information. Keep this vault private, use encrypted device and backup storage, and avoid recording secrets, financial account details, health information, or details another person would not expect you to retain. Before syncing or publishing the repository, confirm that `contacts/` contains only data you intend to share.

## Why Markdown?

Markdown gives you:

- **Ownership** — your relationship data is just files
- **Portability** — works with Obsidian, Logseq, VS Code, or any text editor
- **Longevity** — plain text will still open years from now
- **Control** — no forced workflow, no subscription, no lock-in
- **Simplicity** — the system is only as complicated as you make it

## Why Obsidian Bases?

Obsidian Bases adds database-like views on top of your Markdown notes and note properties.

This repo includes `.base` files for:

- Follow-up reminders
- Contact lists
- Relationship views

You can still use the system without Obsidian Bases, but Bases makes the dashboard much easier.

## Validation

Run the read-only validator before relying on a dashboard:

```text
python3 scripts/validate_contacts.py
```

It checks real contact notes for required properties, valid dates, archive reasons, and unsafe follow-up reminders. It does not edit your files.

## Recommended Vault Setup

Run this as its own Obsidian vault.

Recommended vault name:

```text
People
```

Use the GitHub repo folder itself as the vault folder.

This keeps your networking system separate from your writing, personal notes, and project vaults.

## File Structure

This repo uses a flatter structure on purpose, but real contacts, reviews, samples, and reusable message templates are separated.

```text
crm-markdown/
├── README.md
├── QuickAdd Setup.md
├── Field Definitions.md
├── AI Workflows.md
├── QuickAdd AI Review.md
├── AI Contact Demo.md
├── Company Notes.md
├── Import and Export.md
├── CHANGELOG.md
├── Networking Dashboard.md
├── Follow-Up Dashboard.base
├── Contacts.base
├── contacts/
│   └── README.md
├── reviews/
│   └── README.md
├── message-templates/
│   ├── README.md
│   ├── Warm Check-In.md
│   ├── Follow-Up After No Reply.md
│   ├── Meeting Follow-Up.md
│   ├── Send Resource.md
│   ├── Ask for Introduction.md
│   ├── Make an Introduction.md
│   ├── Thank You.md
│   └── Reconnection.md
├── templates/
│   ├── Contact Template.md
│   ├── Communication Log Entry Template.md
│   ├── Company Template.md
│   ├── Weekly Review Template.md
│   └── Monthly Review Template.md
├── scripts/
│   ├── validate_contacts.py
│   └── test_validate_contacts.py
├── VERSION
├── examples/
│   └── AI Transcript to Contact.md
├── samples/
│   ├── Jane Doe - Acme Inc.md
│   ├── Marcus Lee - Collaborator.md
│   ├── Ana Rivera - Community.md
│   ├── Evelyn Park - Mentor.md
│   ├── Sam Patel - Lead.md
│   └── Lena Brooks - Friend.md
└── archive/
    └── README.md
```

## Where Things Go

### Real Contacts

Put real people in:

```text
contacts/
```

Recommended filename format:

```text
First Last.md
```

Examples:

```text
contacts/Jane Doe.md
contacts/Sam Patel.md
contacts/Evelyn Park.md
```

Do not put real contacts in `samples/`.

### Monthly Reviews

Put monthly relationship reviews in:

```text
reviews/
```

Recommended filename format:

```text
YYYY-MM Monthly Relationship Review.md
```

Example:

```text
reviews/2026-06 Monthly Relationship Review.md
```

### Message Templates

Put reusable networking messages in:

```text
message-templates/
```

These are message templates you might send by email, text, WhatsApp, or DM.

Keep them separate from `templates/`, which is for Obsidian note templates.

### Obsidian Note Templates

Put system templates in:

```text
templates/
```

This folder is for:

- Contact note templates
- Company note templates
- Communication log entry templates
- Monthly review templates

The `samples/` folder is outside the real-contact dashboard scope. Real contacts belong only in `contacts/`.

### Samples

The `samples/` folder contains fake contacts so you can see how the system works.

Delete or ignore them when you are ready to use the vault for real.

### Archive

Move inactive contacts to:

```text
archive/
```

Before archiving a contact, update:

```yaml
status: "archive"
relationship_tier: "archive"
archive_reason: ""
```

## Contact Note Model

Each person gets one contact note.

A contact note includes:

- Contact details
- Relationship type
- Relationship tier
- Follow-up cadence
- Last contacted date
- Next contact due date
- Reason to contact
- Last meaningful topic
- Optional personal fields
- Optional business fields
- Communication log
- Open tasks

## Relationship Types

Use these for `relationship_type`:

- `friend`
- `collaborator`
- `client`
- `lead`
- `mentor`
- `community`

You can add your own, but keep the list small. Too many categories make the system annoying to maintain.

## Relationship Tiers

Use these for `relationship_tier`:

- `core` — people who matter most
- `active` — current clients, collaborators, close peers
- `warm` — good relationships worth maintaining
- `loose` — occasional contact only
- `archive` — inactive or no longer relevant

This is important. Not every contact deserves the same reminder rhythm.

## Contact Cadence

Use these for `contact_cadence`:

- `monthly`
- `quarterly`
- `twice-yearly`
- `yearly`
- `custom`
- `none`

The cadence is the rhythm. The real reminder is `next_contact_due`.

This gives you both structure and flexibility.

## Reminder Dashboard

Open `Networking Dashboard.md` in Obsidian.

It uses the main views from `Follow-Up Dashboard.base`:

- **Contact Today** — people due today
- **Overdue** — people you should have already contacted
- **This Week** — people coming up soon

## Communication Log

Each person has one communication log inside their contact note.

Log meaningful contact, including:

- Email
- Text / WhatsApp
- Phone call
- Zoom call
- In-person meeting
- Commented on their post
- Sent article/resource
- Sent gift/card
- Introduced them to someone
- They contacted you

Do not over-log tiny social media interactions unless they matter. The point is memory and follow-through, not surveillance.

## 30-Second Logging Workflow

After you contact someone, add a short entry like this:

```md
### 2026-06-12 — Email

- **Direction:** Outbound
- **Summary:** Sent a useful article about analog planning.
- **Next step:** Ask how their launch went.
- **Next contact due:** 2026-07-12
```

Then update the properties at the top of the note:

```yaml
last_contacted: 2026-06-12
next_contact_due: 2026-07-12
contact_reason: Ask how their launch went.
last_meaningful_topic: They were preparing a new course launch.
```

That is the whole system.

## QuickAdd Setup

See:

```text
QuickAdd Setup.md
```

Recommended QuickAdd actions:

```text
People: New Contact
People: Log Communication
People: Monthly Review
```

Recommended Mac hotkeys:

```text
Cmd + Option + C  → People: New Contact
Cmd + Shift + L   → People: Log Communication
Cmd + Shift + M   → People: Monthly Review
```

Recommended Windows/Linux hotkeys:

```text
Ctrl + Alt + C    → People: New Contact
Ctrl + Shift + L  → People: Log Communication
Ctrl + Shift + M  → People: Monthly Review
```

## Message Templates

The `message-templates/` folder includes starter templates for value-first networking:

- `Warm Check-In.md`
- `Follow-Up After No Reply.md`
- `Meeting Follow-Up.md`
- `Send Resource.md`
- `Ask for Introduction.md`
- `Make an Introduction.md`
- `Thank You.md`
- `Reconnection.md`

Use these as starting points, not scripts.

Before sending, personalize at least one real detail from the contact note.

The best networking messages should communicate:

- I remembered you.
- I listened.
- I thought this might help.
- I am not trying to pressure you.
- I value the relationship.

## Suggested Workflow

### Daily

Open `Networking Dashboard.md` and check:

1. Contact Today
2. Overdue
3. This Week

Contact only the people who actually make sense today.

### After Contacting Someone

1. Open the contact note.
2. Add one communication log entry.
3. Update `last_contacted`.
4. Update `next_contact_due`.
5. Update `contact_reason` if there is a clear next reason.

### Monthly

Use `templates/Monthly Review Template.md` or QuickAdd’s `People: Monthly Review` action to review:

- Who you contacted
- Who you neglected
- Which relationships matter now
- Who should be archived
- Who deserves more attention next month
- What resources, introductions, or thank-you notes you should send

## How to Start

1. Clone or download this repo.
2. Open this folder as its own Obsidian vault.
3. Name the vault `People` if you want a simple, human name.
4. Turn on the **Bases** core plugin in Obsidian.
5. Install QuickAdd if you want fast capture workflows.
6. Open `Networking Dashboard.md`.
7. Review the sample contacts.
8. Duplicate `templates/Contact Template.md` or use QuickAdd to create your first real contact.
9. Put real contacts in `contacts/`.
10. Delete the sample contacts when you no longer need them.

## Recommended Obsidian Setup

Recommended theme:

```text
Minimal
```

Recommended core plugins:

- Bases
- Templates
- Backlinks
- Page Preview
- File Recovery

Recommended community plugins:

- Minimal Theme Settings
- QuickAdd
- Obsidian Git, if you want GitHub sync/versioning

Optional later:

- Tasks, only if contact-note tasks become hard to manage

Avoid adding too many plugins at first. This vault should stay fast and calm.

## Using Without Obsidian

You can still use this system in any Markdown editor.

Without Obsidian Bases, use search for:

```text
next_contact_due: 2026-06
relationship_tier: core
relationship_type: mentor
```

The data is still plain Markdown.

## Recommended Rules

- Keep one note per person.
- Put real contacts in `contacts/`.
- Keep the communication log inside that person’s note.
- Update the next due date manually.
- Use cadence as guidance, not law.
- Use message templates as starting points, not scripts.
- Personalize every message before sending.
- Share resources when they are truly useful.
- Make introductions with care.
- Say thank you specifically.
- Archive people without guilt.
- Do not turn this into a second inbox.
- Do not over-track people.
- Keep it human.

## Customization

You can add:

- More relationship types
- More sample people
- More message templates
- More `.base` views
- Scripts for automatic due-date updates
- Dataview queries if you prefer Dataview
- Sync using Git, iCloud, Dropbox, Syncthing, or Obsidian Sync

But start simple first.

## License

This project is licensed under the GPL-2.0 License.

## Final Thought

A good networking system should help you be more thoughtful, not more mechanical.

Use this to remember people, follow up when it matters, share what is useful, make meaningful introductions, and build stronger relationships without turning your life into a sales dashboard.
