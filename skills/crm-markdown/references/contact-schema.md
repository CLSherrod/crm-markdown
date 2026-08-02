# Contact Schema Reference

## Required fields

```yaml
type: contact
name: ""
status: inbox | review | active | inactive | archive
relationship_tier: core | active | warm | dormant
last_contacted: "YYYY-MM-DD or blank"
next_contact_due: "YYYY-MM-DD or blank"
do_not_contact: false
```

## Common fields

```yaml
company: ""
role: ""
email: ""
phone: ""
website: ""
location: ""
timezone: ""
social_links: []
relationship_type: ""
profile_complete: false
contact_cadence: monthly | quarterly | yearly | custom
preferred_contact_method: email | text / whatsapp | phone | in-person
contact_reason: ""
last_meaningful_topic: ""
archive_reason: ""
```

Use the existing template as the source of truth when fields evolve. Do not add speculative values merely to complete the schema.
