# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without requiring the program to be executed. Tools such as Pylint, Flake8, and Bandit identify potential problems involving code quality, style, maintainability, and security. It helps developers detect issues early, improve readability, and reduce the likelihood of defects.

## 2. What did Pylint, Flake8, and Bandit identify?

Pylint identified code-quality problems such as missing docstrings, inconsistent naming, unused imports and variables, a mutable default argument, unsafe expression evaluation, and poor exception handling. Flake8 identified style and formatting violations. Bandit identified security concerns, including the use of eval(), shell command execution, MD5 hashing, and a non-cryptographic random-number generator for token generation.

## 3. What changes did you make to fix the issues?

I replaced eval() with a numeric multiplier and input validation, removed shell command execution, replaced MD5 with SHA-256, and used the secrets module for token generation. I also improved exception handling, replaced the mutable default list with None, used a context manager for file operations, added docstrings, improved naming, and removed unused imports and variables.

These changes improved the code's readability and addressed the issues identified by the static-analysis tools while preserving the program's core functionality.

## 4. What were the results, and what did you learn?

After modifying the program, I ran it successfully and reran all three analysis tools. Pylint reported a score of 10.00/10, Flake8 reported no violations, and Bandit identified no issues.

This lab taught me that static-analysis tools can identify problems that may not be obvious during normal execution. I also learned that fixing code quality and security issues makes programs easier to maintain. However, passing static analysis does not guarantee that software is completely secure or free of bugs, so testing and code review remain important.
