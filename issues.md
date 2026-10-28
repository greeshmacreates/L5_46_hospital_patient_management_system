# Lab 5: Static Code Analysis — Issue Report

The following issues were identified in the original version of `hospital_patient_system.py` using Pylint, Flake8, and Bandit. Issues are prioritized by severity.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe use of eval() | Security — High | 35 | `eval()` can execute arbitrary Python code when given untrusted input. | Replaced expression evaluation with a numeric multiplier and explicit validation. |
| Shell command injection risk | Security — High | 48 | `os.system()` constructs a shell command using a filename, creating a potential command injection vulnerability. | Removed the shell command and used a normal Python `print()` statement. |
| Weak MD5 hash | Security — High | 39 | MD5 is cryptographically broken and unsuitable when a stronger digest is required. | Replaced MD5 with SHA-256. Hashing a predictable patient ID does not make it confidential. |
| Bare exception handling | Error handling — Medium | 21–22 | A bare `except` silently catches unexpected errors and makes failures difficult to diagnose. | Used an explicit patient lookup and returned a status for unknown patient IDs. |
| Mutable default argument | Code quality | 11 | `intake_log=[]` creates a shared mutable default list. | Changed the default to `None` and append only when a log is provided. |
| Unsafe file handling | Code quality | 45–47 | Manual file closing can fail to occur if an exception happens during writing. | Used a context manager and UTF-8 encoding. |
| Incorrect None comparison | Code quality | 26 | Using `== None` is less appropriate than checking object identity. | Used an explicit `is None` check in the revised logic. |
| Missing documentation and naming/style issues | Code quality | Multiple | Missing docstrings, inconsistent naming, unused code, and older string formatting reduced maintainability. | Added docstrings, used snake_case, removed unused imports and variables, and used f-strings. |
| Weak random token generation | Security | 42 | `random.randint()` is not designed for security-sensitive token generation. | Replaced it with `secrets.randbelow()`. |

## Verification

- Pylint: 10.00/10
- Flake8: No reported violations
- Bandit: No identified issues
- Program execution: Successful

These results confirm that the current file passes the checks performed by these tools, but they do not guarantee that the application is free of all bugs or security vulnerabilities.
