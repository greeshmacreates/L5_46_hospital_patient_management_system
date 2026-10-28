# Lab 5: Static Code Analysis — Issue Report

The following issues were identified in the original version of `hospital_patient_system.py` using Pylint, Flake8, and Bandit. Issues are prioritized by severity.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command injection risk | Security — High | 55 | `os.system()` constructs a shell command using a filename, creating a potential command injection vulnerability. | Removed the shell command and used a normal Python `print()` statement. |
| Weak MD5 hash | Security — High | 44 | MD5 is cryptographically broken and unsuitable when a stronger digest is required. | Replaced MD5 with SHA-256. Hashing a predictable patient ID does not make it confidential. |
| Unsafe use of eval() | Security — Medium | 35 | `eval()` can execute arbitrary Python code when given untrusted input. | Replaced expression evaluation with a numeric multiplier and explicit type and range validation. |
| Bare exception handling | Error handling — Medium | 23–24 | A bare `except` silently catches unexpected errors and makes failures difficult to diagnose. | Used an explicit patient lookup and returned a status for unknown patient IDs. |
| Weak random token generation | Security — Low | 48 | `random.randint()` is not designed for security-sensitive token generation. | Replaced it with `secrets.randbelow()`. |
| Mutable default argument | Code quality | 12 | `intake_log=[]` creates a shared mutable default list. | Changed the default to `None` and append only when a log is provided. |
| Unsafe file handling | Code quality | 52–54 | Manual file closing may not occur if an exception happens during writing. | Used a context manager and UTF-8 encoding. |
| Incorrect None comparison | Code quality | 29 | Using `== None` is less appropriate than checking object identity. | Used an explicit `is None` check in the revised logic. |
| Missing documentation and naming/style issues | Code quality | Multiple | Missing docstrings, inconsistent naming, unused imports and variables, and older string formatting reduced maintainability. | Added docstrings, used snake_case, removed unused code, and used f-strings. |

## Verification

- Pylint: 10.00/10
- Flake8: No reported violations
- Bandit: No identified issues
- Program execution: Successful

These results confirm that the current file passes the checks performed by these tools, but they do not guarantee that the application is free of all bugs or security vulnerabilities.
