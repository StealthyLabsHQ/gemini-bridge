---
description: Query Gemini with a specific model tier. Usage: /gemini:model <lite|flash|pro> <prompt>
---

Parse `$ARGUMENTS` as follows: the **first word** is the tier (`lite`, `flash`, or `pro`), and **everything after** is the prompt.

Call the MCP tool `query_gemini` with the extracted `tier` and `prompt`.

Examples:
- `/gemini:model flash what is the difference between TCP and UDP?` → tier=flash
- `/gemini:model pro review this architecture` → tier=pro
- `/gemini:model lite quick summary of this` → tier=lite

If no arguments are provided, ask the user for the tier and prompt.
If only a tier is provided with no prompt, ask for the prompt.
If an invalid tier is given, inform the user and ask them to choose: lite, flash, or pro.
