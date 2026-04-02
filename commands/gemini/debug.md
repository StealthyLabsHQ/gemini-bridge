---
description: Send an error or stack trace to Gemini for diagnosis. Usage: /gemini:debug <error> [-- context]
---

Call the MCP tool `debug_error` with the provided error or stack trace.

If `$ARGUMENTS` contains `--` as a separator, split it: the part before `--` is the `error`, the part after is the `context`.

Otherwise, pass all of `$ARGUMENTS` as the `error` parameter.

If no arguments are provided, ask the user to paste the error or stack trace they want diagnosed.

Present Gemini's diagnosis clearly: root cause first, then the fix, then alternatives if any.
