# Import and Export

This system is intentionally plain Markdown, so information can be moved in and out with a review step.

## Business Cards and Email Signatures

Ask AI to extract only observable fields:

```text
Extract contact information from this business card or email signature.
Return Markdown YAML fields for name, company, role, email, phone, website, location, and social_links.
Leave unknown fields blank. Do not infer anything. Add status: "review" and profile_complete: false.
Source:
[PASTE REDACTED TEXT]
```

## CSV Imports

Map common columns as follows:

| Source column | Contact field |
| --- | --- |
| Full Name | `name` |
| Company | `company` |
| Job Title | `role` |
| Email | `email` |
| Phone | `phone` |
| Website | `website` |
| City / Country | `location` |
| Tags | `crm_tags` |

Set imported records to `status: "review"`. Do not assign a cadence or follow-up date until the relationship has been reviewed.

## Exporting

Because each contact is a Markdown file with YAML frontmatter, keep the original files as the source of truth. For a spreadsheet export, use only the fields needed for the purpose and avoid exporting personal notes, family information, or sensitive history.

Always review the destination before uploading contact data to another service.
