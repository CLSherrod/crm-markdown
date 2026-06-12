# Networking Dashboard

Use this page as your daily relationship check-in.

The system is simple:

1. Contact the people due today.
2. Clear anything overdue.
3. Look ahead at this week.
4. Log the interaction inside that person’s note.
5. Update `last_contacted` and `next_contact_due`.

## Contact Today

```base
filters:
  and:
    - type == "contact"
    - status != "archive"
    - next_contact_due == date(today)
views:
  - type: table
    name: Contact Today
    order:
      - file.name
      - relationship_type
      - relationship_tier
      - preferred_contact_method
      - contact_reason
      - last_contacted
      - next_contact_due
    sort:
      - property: relationship_tier
        direction: ASC
      - property: file.name
        direction: ASC
```

## Overdue

```base
filters:
  and:
    - type == "contact"
    - status != "archive"
    - next_contact_due < date(today)
views:
  - type: table
    name: Overdue
    order:
      - file.name
      - relationship_type
      - relationship_tier
      - preferred_contact_method
      - contact_reason
      - last_contacted
      - next_contact_due
    sort:
      - property: next_contact_due
        direction: ASC
```

## This Week

```base
filters:
  and:
    - type == "contact"
    - status != "archive"
    - next_contact_due > date(today)
    - next_contact_due <= date(today) + dur(7 days)
views:
  - type: table
    name: This Week
    order:
      - file.name
      - relationship_type
      - relationship_tier
      - preferred_contact_method
      - contact_reason
      - last_contacted
      - next_contact_due
    sort:
      - property: next_contact_due
        direction: ASC
```

## Monthly Review

Once a month, duplicate `templates/Monthly Review Template.md` and answer the prompts.

The goal is not to contact everyone. The goal is to maintain the relationships that still matter.
