---
description: Review code with Gemini. Usage: /gemini:review [file or code snippet]
---

Review code using Gemini via the MCP tool `review_code`.

If `$ARGUMENTS` contains a file path, read that file first, then call `review_code(code=<file_contents>, language=<detected_language>, tier="pro")`.

If `$ARGUMENTS` is a code snippet, call `review_code(code="$ARGUMENTS", tier="pro")` directly.

If no arguments are provided, ask the user which file or code they want reviewed.

After getting Gemini's response, summarize the findings clearly: list CRITICAL issues first, then WARNING, then SUGGESTION.
