# Fix Validation — Task 2

## Method and scope

Applied the targeted changes proposed in `ai_debug_log.md` to copies under `bug_fixes/`. The intentionally vulnerable originals in `bug_snippets/` were left unchanged. Tests were executed locally using Python `unittest`, Node.js `assert` and a standalone Java test harness. Results below report observed executions, not hypothetical outcomes. These are classroom-scale examples, not production security certification.

## File locations and validation mapping

All paths below are relative to the repository's `smart_bug_bounty/` directory. The corrected files are **inside `bug_fixes/`**, not at the repository root. A filename shown without its directory (such as `bug2_fixed.js`) is the basename of `bug_fixes/bug2_fixed.js`.

| Original file | Fixed filename | Repository-relative location | Tests passed |
| --- | --- | --- | ---: |
| `bug1.py` | `bug1_fixed.py` | `bug_fixes/bug1_fixed.py` | 4 |
| `bug2.js` | `bug2_fixed.js` | `bug_fixes/bug2_fixed.js` | 4 |
| `bug3.java` | `bug3_fixed.java` | `bug_fixes/bug3_fixed.java` | 4 |
| `bug4.py` | `bug4_fixed.py` | `bug_fixes/bug4_fixed.py` | 7 |
| `bug5.js` | `bug5_fixed.js` | `bug_fixes/bug5_fixed.js` | 5 |

## `bug1.py` — SQL injection

- **Original Issue:** Untrusted username text was concatenated into SQL syntax.
- **Fix Applied:** Replaced concatenation with a bound `?` query parameter in `bug_fixes/bug1_fixed.py`.
- **Test Results:** **4 passed** — known account, second known account, unknown account and injection-shaped input treated as literal text.
- **Security Result:** The tested input cannot alter the SQL statement's structure.

## `bug2.js` — XSS through unsafe HTML insertion

- **Original Issue:** User-controlled name was inserted using `innerHTML`.
- **Fix Applied:** Created a paragraph with `ownerDocument.createElement('p')`, assigned its `textContent` and replaced existing children in `bug_fixes/bug2_fixed.js`.
- **Test Results:** **4 passed** — normal name, HTML-like payload, non-string input and replacement of existing content.
- **Validation Limitation:** Executed in Node.js using a small DOM test double that models escaping and records DOM API calls. This is **not a real-browser DOM security test**. Browser verification remains advisable before production use.

## `bug3.java` — broken access control

- **Original Issue:** `readDocument()` returned document content without checking the requesting user.
- **Fix Applied:** Added a null-safe ownership comparison and returned `ACCESS_DENIED` for non-owners in `bug_fixes/bug3_fixed.java`.
- **Test Results:** **4 passed** — owner allowed, non-owner denied, missing document and null user denied.
- **Security Result:** The local document function enforces ownership. In production, the `user` identity must be derived from a trusted authentication context.

## `bug4.py` — plaintext password storage

- **Original Issue:** Account records stored raw passwords and compared them directly.
- **Fix Applied:** Replaced plaintext with a per-account random 16-byte salt and `hashlib.scrypt` password verifier, checked using `hmac.compare_digest`, in `bug_fixes/bug4_fixed.py`.
- **Test Results:** **7 passed** — correct password, wrong password, unknown account, no plaintext field, duplicate username, missing input and distinct salts/verifiers for separate accounts.
- **Security Result:** Raw passwords are not retained in the account record. The parameters are for a dependency-free demonstration; production use requires environment-specific password-hashing review and appropriate operational controls.

## `bug5.js` — missing reset-request rate limit

- **Original Issue:** Every superficially valid request was queued without any frequency check.
- **Fix Applied:** Implemented a per-normalized-email, in-memory rolling-window limiter: **3 accepted requests per 60,000 ms**; excess requests return `429` and are not queued in `bug_fixes/bug5_fixed.js`.
- **Test Results:** **5 passed** — first three accepted/fourth denied, expiry at the window boundary, separate accounts, case-insensitive keying and invalid input handling.
- **Security Result:** The agreed classroom threshold is enforced for the tested cases. This is not a production-ready distributed limiter: timestamps are supplied by the caller for deterministic testing and state is process-local. A production implementation needs a trusted server clock, shared/bounded state and additional abuse protections.

## Execution evidence

Run from the `smart_bug_bounty/` directory:

```bash
python3 -m unittest discover -s validation_tests -p 'test_python_fixes.py' -v
node validation_tests/test_javascript_fixes.js
mkdir -p /tmp/bfb_java
javac -d /tmp/bfb_java bug_fixes/bug3_fixed.java validation_tests/TestBug3Fixed.java
java -cp /tmp/bfb_java TestBug3Fixed
```

| Test suite | Observed result |
| --- | --- |
| Python `unittest` | 11 tests passed (`OK`) |
| JavaScript Node.js assertions | 9 tests passed |
| Java test harness | 4 tests passed |
| **Total** | **24 tests passed, 0 failures** |

**Conclusion:** All five fixes passed the executed local automated checks. Browser-level DOM verification and production deployment review are outside the completed validation scope.
