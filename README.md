# CRM in Markdown

A simple, local-first networking and lightweight CRM system built entirely with Markdown files.

No subscriptions. No lock-in. No bloated sales pipeline. Just plain text you control.

This project is designed for people who want to remember people, follow up with care, and keep a useful communication history without handing their relationship data to another SaaS platform.

## What This Is

**CRM in Markdown** is a Markdown-first, Obsidian-enhanced networking system.

It helps you track:

- Friends
- Collaborators
- Clients
- Leads
- Mentors
- Community relationships

The system is intentionally simple: **one person = one contact note**. Each contact note includes the person’s profile, follow-up rhythm, next contact date, and communication log.

## What This Is Not

This is not a heavy sales CRM.

It does not try to replace Salesforce, HubSpot, or a full business automation platform. It is a calm, human-scale system for staying in touch with people who matter.

## Core Philosophy

Most networking systems fail because they become another job.

This system is built around a 30-second habit:

1. Open the person’s contact note.
2. Add a short communication log entry.
3. Update `last_contacted`.
4. Update `next_contact_due`.
5. Move on.

Consistency matters more than complexity.

## Features

- **One Markdown file per person**
- **One communication log per person**
- **Monthly, quarterly, yearly, and custom follow-up cadences**
- **Manual next-contact dates for real flexibility**
- **Obsidian Bases dashboards for reminders**
- **Contact Today, Overdue, and This Week views**
- **Relationship tiers so not everyone gets the same attention**
- **Personal and business fields**
- **Templates for contacts, companies, logs, and monthly reviews**
- **Example data you can delete or adapt**

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

## File Structure

This repo uses a flatter structure on purpose.

```text
crm-markdown/
├── README.md
├── Networking Dashboard.md
├── Follow-Up Dashboard.base
├── Contacts.base
├── templates/
│   ├── Contact Template.md
│   ├── Communication Log Entry Template.md
│   ├── Company Template.md
│   └── Monthly Review Template.md
├── samples/
│   ├── Jane Doe - Acme Inc.md
│   ├── Marcus Lee - Collaborator.md
│   ├── Ana Rivera - Community.md
│   ├── Evelyn Park - Mentor.md
│   ├── Sam Patel - Lead.md
│   └── Lena Brooks - Friend.md
└── archive/
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

It embeds the main views from `Follow-Up Dashboard.base`:

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

Use `templates/Monthly Review Template.md` to review:

- Who you contacted
- Who you neglected
- Which relationships matter now
- Who should be archived
- Who deserves more attention next month

## How to Start

1. Open this folder as an Obsidian vault.
2. Turn on the **Bases** core plugin in Obsidian.
3. Open `Networking Dashboard.md`.
4. Review the sample contacts.
5. Duplicate `templates/Contact Template.md` for your first real contact.
6. Delete the sample contacts when you no longer need them.

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
- Keep the communication log inside that person’s note.
- Update the next due date manually.
- Use cadence as guidance, not law.
- Archive people without guilt.
- Do not turn this into a second inbox.
- Do not over-track people.
- Keep it human.

## Customization

You can add:

- More relationship types
- More sample people
- More `.base` views
- Scripts for automatic due-date updates
- Dataview queries if you prefer Dataview
- Sync using Git, iCloud, Dropbox, Syncthing, or Obsidian Sync

But start simple first.

## License

This project is licensed under the GPL-2.0 License.

## Final Thought

A good networking system should help you be more thoughtful, not more mechanical.

Use this to remember people, follow up when it matters, and build stronger relationships without turning your life into a sales dashboard.
