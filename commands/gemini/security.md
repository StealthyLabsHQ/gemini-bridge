---
description: Security audit of code with Gemini Pro (OWASP, secrets, injections). Usage: /gemini:security <file or code>
---

Run a security audit using Gemini via the MCP tool `security_audit`.

If `$ARGUMENTS` contains a file path, read that file first, then call `security_audit(code=<file_contents>, language=<detected_language>, tier="pro")`.

If `$ARGUMENTS` is a code snippet, call `security_audit(code="$ARGUMENTS", tier="pro")` directly.

If no arguments are provided, ask the user which file or code they want audited.

After receiving Gemini's response, present findings ordered by severity: CRITICAL → HIGH → MEDIUM → LOW. If the result is CLEAN, confirm that clearly.
