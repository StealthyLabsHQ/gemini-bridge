---
description: View or change Gemini settings (thinking, temperature, media, tokens). Usage: /gemini:config [setting] [value]
---

Call the MCP tool `configure_gemini` based on the arguments provided.

- No arguments → `configure_gemini()` — show all current settings
- One argument (setting name) → `configure_gemini(setting="$ARGUMENTS")` — show current value of that setting
- Two arguments (setting + value) → `configure_gemini(setting=<first>, value=<second>)` — update the setting

Supported settings and values:
- `thinking` → OFF / LOW / MEDIUM / HIGH
- `temperature` → 0.0 to 2.0
- `media` → LOW / MEDIUM / HIGH
- `tokens` → 1 to 65536
- `top_p` → 0.0 to 1.0

Display the result clearly. If updated, confirm the new value is active immediately.
