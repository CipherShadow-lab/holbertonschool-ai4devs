# Bug Descriptions

This project contains five **intentionally vulnerable, self-contained educational snippets**. Each original file is retained unchanged for AI-assisted investigation in Task 1 and comparison with corrected code in Task 2. Use only local, synthetic test data.  

## `bug1.py` - SQL Injection (Python)
- **Intended Behavior**: Look up the role for the exact username supplied. Unknown usernames should return `None` without changing query meaning.
- **Current Issue**: The SQL statement concatenates user-controlled text into a query, allowing input to alter SQL interpretation.
- **Test Focus**: Known username, unknown username and a specially formatted username that must be treated as literal data.  

## `bug2.js` - Unsafe HTML Rendering / XSS (JavaScript)
- **Intended Behavior**: Display the supplied profile name as plain text without interpreting markup or executable content.
- **Current Issue**: The renderer interpolates untrusted text into `innerHTML`, which the browser parses as HTML.
- **Test Focus**: Normal name, a name containing HTML markup and non-string input.  

## `bug3.java` - Broken Access Control (Java)
- **Intended Behavior**: Return a document only to its owner; missing documents should return `NOT_FOUND` and access by another user should be denied.
- **Current Issue**: The lookup verifies document existence but does not check the requesting user's identity against the document owner.
- **Test Focus**: Owner access, non-owner access and missing document.  

## `bug4.py` - Insecure Password Storage (Python)
- **Intended Behavior**: Register accounts without retaining plaintext passwords, and verify later login attempts against a securely stored password representation.
- **Current Issue**: Passwords are saved directly in the account dictionary and compared as plaintext.
- **Test Focus**: Registration, correct and incorrect password verification, duplicate usernames and absence of plaintext in stored records.  

## `bug5.js` - Missing Rate Limiting (JavaScript)
- **Intended Behavior**: Accept valid password-reset requests while limiting repeated requests for the same account within a defined time window.
- **Current Issue**: Every valid request is queued, regardless of how frequently that account has requested a reset.
- **Test Focus**: First request, repeated requests within the window, request after the window and invalid inputs.  

## Scope and Safety

- The examples are intentionally flawed for a local debugging exercise and educational purposes only; **these should NOT be deployed**.
- No real user accounts, passwords, network targets or external services are needed.
- Task 0 documents the intended behavior and current issues. Task 1 will record AI explanations, suggested fixes and confidence levels. Task 2 will implement fixes and report actual test outcomes.
- A passing functional test alone does not establish that a security issue has been resolved; negative security tests are essential.  
