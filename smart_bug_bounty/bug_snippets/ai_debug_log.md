# AI Debug Log

## Method

### Prompt-engineering approach

The coursework provides a baseline question: “This code throws an error / doesn’t behave as expected. Can you identify and explain the issue and how to fix it?”  
For a more rigorous security-focused review, the following **enhanced reusable prompt** formalizes the analysis criteria for the five snippets. It specifies the reviewer’s role, evidence boundaries, expected output and how uncertainty should be handled. It is documented here as an improved prompt template; the findings below are AI-assisted source reviews, not proof that this exact wording was used verbatim in the initial analysis.

### Enhanced Security Debugging Prompt

> **Role:** Act as a senior application security engineer and secure-code reviewer experienced in Python, JavaScript and Java. Apply defensive programming principles and relevant OWASP secure-code-review practices.
>
> **Objective:** Review the supplied code for functional defects and security weaknesses. Explain the root cause and propose the smallest appropriate correction that preserves the documented intended behaviour.
>
> **Evidence and scope:** Base conclusions only on the supplied source code and stated requirements. Do not invent runtime results, surrounding architecture, dependencies, exploitability conditions or security controls. Explicitly distinguish directly observed facts from plausible risks and missing context. If information is insufficient, state what would need verification rather than silently assuming it.
>
> **Review procedure:** (1) Summarise the intended behaviour; (2) identify the exact defective operation or missing check; (3) trace relevant untrusted inputs, data flow and trust boundaries; (4) explain the impact and any conditions required for it; (5) recommend a language-appropriate, minimal fix; (6) identify potential regressions and relevant positive, negative and boundary tests.
>
> **Output format:** For each file, provide **AI Explanation**, **Root Cause**, **Suggested Fix**, **Confidence** (High/Medium/Low with a concise justification) and **Task 2 Validation Plan**. Include code-level evidence where possible. Explain limitations and do not claim tests have passed unless execution results are supplied.
>
> **Constraints:** Do not modify the original snippet. Avoid speculative findings, unnecessary refactoring, new dependencies or scope creep. Treat confidence as an assessment of the evidence, not a guarantee of correctness.
>
> **Input:** Filename, programming language, intended behaviour and the complete original snippet follow below.

### Review Controls and Limitations

Each original snippet in `bug_snippets/` was examined with ChatGPT against its intended behaviour. The enhanced prompt above provides a reproducible standard for follow-up review and future debugging sessions. The findings below distinguish source-supported diagnoses from design choices requiring confirmation (such as the rate-limit threshold). **No fixes have been applied to the originals.** Task 2 will implement and validate the proposed corrections with positive, negative and boundary tests.

**Reference:** OWASP, *Secure Code Review Cheat Sheet* — https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html (review methodology, data-flow analysis and trust boundaries).

## `bug1.py` — SQL Injection (Python)

- **AI Explanation**: `find_role()` builds a SQL query by concatenating `username` between SQL quotes. A specially formatted username can therefore change the query's meaning rather than being matched as a literal username. A normal lookup may work, concealing the defect.
- **Root Cause**: Untrusted data is embedded in SQL syntax rather than bound as a query parameter.
- **Suggested Fix**: Replace the concatenation with `connection.execute("SELECT role FROM accounts WHERE username = ?", (username,))`. Keep the existing `None` response for unknown users.
- **Confidence**: **High** — The unsafe string concatenation is explicit in the source; the proposed parameter-binding pattern is standard for Python's `sqlite3`.
- **Task 2 Validation Plan**: Verify the known user, unknown user and a specially formatted username are all handled as exact values; ensure the latter cannot change query semantics.

## `bug2.js` — Unsafe HTML Rendering / XSS (JavaScript)

- **AI Explanation**: `renderProfile()` inserts an untrusted name into `outputElement.innerHTML`. The browser parses markup in the name instead of displaying it literally. The type check ensures a string, but does not make its contents safe HTML.
- **Root Cause**: Use of an HTML-parsing DOM sink for plain-text user content.
- **Suggested Fix**: Create a `p` element, assign the name with `paragraph.textContent = `Welcome, ${name}``, then replace the target's children with `outputElement.replaceChildren(paragraph)`. Retain the non-string input check. If returning HTML is part of the interface, the resulting `outputElement.innerHTML` will contain escaped markup for the name.
- **Confidence**: **High** — The vulnerable `innerHTML` assignment is explicit. Browser/DOM testing is still required to verify the replacement.
- **Task 2 Validation Plan**: Test a normal name, a string containing HTML-like markup and a non-string value in a DOM-capable environment; confirm the input is displayed as text rather than parsed as elements.

## `bug3.java` — Broken Access Control (Java)

- **AI Explanation**: `readDocument()` checks only whether the document ID exists. The `user` parameter is never used, so any caller with a known document ID can read another user's content. The example in `main()` passes `sam` for a document owned by `alex`.
- **Root Cause**: Missing per-document ownership authorization after lookup.
- **Suggested Fix**: After the missing-document check, compare the requesting user with `document.owner` using a null-safe value comparison, such as `document.owner.equals(user)` when owners are guaranteed non-null. Return `ACCESS_DENIED` for non-owners and retain `NOT_FOUND` for missing IDs. In a real service, the requesting identity must come from a trusted authentication context, not an untrusted caller-supplied name.
- **Confidence**: **High** — The unused `user` parameter and missing ownership condition are directly visible.
- **Task 2 Validation Plan**: Verify the owner can read, a different user receives `ACCESS_DENIED` and a missing ID receives `NOT_FOUND`.

## `bug4.py` — Insecure Password Storage (Python)

- **AI Explanation**: `register_user()` stores the password directly in `accounts[username]["password"]`, and `verify_password()` compares the submitted password against that plaintext. A disclosure of the dictionary would expose the original passwords.
- **Root Cause**: Storing reusable credentials instead of a password-specific, salted, computationally expensive verifier.
- **Suggested Fix**: Store a unique random salt and a derived password hash rather than plaintext. For a dependency-free classroom implementation, Python's `hashlib.scrypt` with `secrets.token_bytes` is a reasonable choice, subject to environment support; use `hmac.compare_digest` when comparing derived values. A production system should use a vetted password-hashing library and appropriately configured parameters (for example Argon2id where available). Preserve duplicate-account and missing-input validation.
- **Confidence**: **High** for the plaintext-storage diagnosis; **Medium** for the specific implementation until its parameters, runtime compatibility and tests are verified.
- **Task 2 Validation Plan**: Test registration, correct and incorrect passwords, duplicate usernames and that the stored record does not contain the plaintext password; verify different registrations use distinct salts.

## `bug5.js` — Missing Rate Limiting (JavaScript)

- **AI Explanation**: Every request with a superficially valid email and finite timestamp is appended to `queuedRequests`. There is no count, cooldown or window check, so repeated requests for the same email are always accepted.
- **Root Cause**: No per-account request-frequency control before queuing a reset request.
- **Suggested Fix**: Define a specific policy before implementation (proposed classroom policy: **at most three accepted requests per email per rolling 60,000 ms**). Track accepted request timestamps per normalized email, discard timestamps outside the active window and return a throttling response (for example HTTP-style status `429`) once the limit is reached. Keep invalid-input checks. The supplied `nowMs` is a testing convenience and must not be trusted from a real external client; production implementations also require shared, bounded state and abuse controls.
- **Confidence**: **High** for the missing limiter; **Medium** for the proposed policy because the coursework does not specify a threshold and the policy must be agreed before Task 2.
- **Task 2 Validation Plan**: Test the first three accepted requests, the fourth within the window, a request after the window, independent email accounts and invalid inputs. Verify rejected requests are not queued.

## Review Summary

The five findings cover SQL injection, DOM-based XSS, broken access control, plaintext password storage and missing rate limiting. Confidence ratings describe how strongly the source supports each diagnosis and suggestion; they are **not** evidence that a fix has passed tests. Task 2 will preserve the vulnerable originals, place corrected copies in `bug_fixes/` and record executed test results in `fix_validation.md`.
