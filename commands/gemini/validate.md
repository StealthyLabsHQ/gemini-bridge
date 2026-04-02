---
description: Validate a plan with Gemini Pro before executing it. Usage: /gemini:validate <plan description>
---

Call the MCP tool `validate_plan` with `plan="$ARGUMENTS"` and `tier="pro"`.

Display Gemini's verdict clearly:
- List CRITICAL findings first (these block execution)
- Then WARNING findings (should address)
- Then SUGGESTION findings (optional)
- End with the final verdict: PROCEED / REVISE / DO NOT PROCEED

If no arguments are provided, ask the user to describe the plan they want validated.
