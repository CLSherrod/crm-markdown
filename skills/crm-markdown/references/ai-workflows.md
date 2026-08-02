# AI Workflow Reference

## Contact draft

Ask AI to return a proposed YAML block, a short snapshot, missing information, and suggested relationship fields. Require `status: "review"`, `profile_complete: false`, and no invented dates.

## To-do extraction

Ask AI to return only explicitly promised or requested actions, separated by owner. Mark unclear ownership and deadlines as `needs confirmation`.

## Information request

Ask AI for a short message requesting only the missing fields, with an easy way for the person to decline or share less.

## Existing-note update

Ask AI to return only changed fields, a new log entry, confirmed tasks, and unanswered questions. Never request a full rewritten note when a narrow patch will do.

For complete prompts, use `AI Workflows.md` in the repository root.
