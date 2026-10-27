# Lab 5: Static Code Analysis

## 1. Objective

To analyze and improve a Python program using Pylint, Bandit, and Flake8, document the identified issues, and compare static analysis reports before and after fixing the issues.

## 2. Issue Documentation

| Tool | Issue Identified | Correction |
|---|---|---|
| Pylint | Missing module and function docstrings | Added descriptive docstrings |
| Pylint | Mutable default argument | Replaced the shared list default with `None` |
| Pylint | Naming and code quality issues | Improved naming and code organization |
| Bandit | SQL query string concatenation | Replaced concatenation with parameterized SQL |
| Bandit | Insecure random-number generation | Used Python's `secrets` module |
| Bandit | Broad exception handling | Caught `sqlite3.Error` and reported the error |
| Flake8 | Long lines and trailing whitespace | Improved formatting and removed unnecessary whitespace |
| Flake8 | Unused variables and improper `None` comparison | Removed unused variables and used `is None` |

## 3. Static Analysis Results

- **Pylint:** Final score of 10.00/10.
- **Bandit:** No security issues identified.
- **Flake8:** No reported style violations.

## 4. Reflection Questions and Answers

### Q1. What is static code analysis, and why is it important?

Static code analysis examines source code without executing the program to identify potential errors, security vulnerabilities, and coding style violations. It helps improve code quality, readability, maintainability, and security.

### Q2. What are the purposes of Pylint, Bandit, and Flake8?

Pylint checks code quality, programming errors, naming conventions, and documentation. Bandit identifies potential security vulnerabilities in Python code. Flake8 detects coding style violations, formatting issues, and certain programming errors.

### Q3. What issues were identified in the original program, and how were they fixed?

The original bike-share station program contained missing docstrings, a mutable default argument, SQL query string concatenation, insecure random-number generation, broad exception handling, and formatting violations. These issues were addressed by improving documentation and formatting, using `None` for the default list argument, parameterized SQL queries, the `secrets` module for PIN generation, and specific SQLite exception handling.

### Q4. What did you learn from this lab?

I learned how to use Pylint, Bandit, and Flake8 to improve Python code quality, security, and formatting. I also learned the importance of secure SQL queries, proper exception handling, and Git version control. After making the corrections, the program achieved a Pylint score of 10.00/10, Bandit reported no security issues, and Flake8 reported no violations.

## 5. Before-and-After Reports

The repository contains the following reports for comparison:

- `pylint_before.txt`
- `pylint_after.txt`
- `bandit_before.txt`
- `bandit_after.txt`
- `flake8_before.txt`
- `flake8_after.txt`
