# Smart Bug Bounty

Security-focused debugging exercise for Holberton AI-assisted development coursework.

- **Task 0**: `bug_snippets/` contains five intentionally flawed source files; `bug_descriptions.md` documents intended behavior and observed weaknesses.  
  
- **Task 1**: Record AI-assisted diagnosis in `ai_debug_log.md` (to be created during Task 1).  
  
- **Task 2**: Add corrected versions under `bug_fixes/` and record executed tests in `fix_validation.md` (to be created during Task 2).  

## Local Checks

- Python: `python3 bug_snippets/bug1.py` and `python3 bug_snippets/bug4.py`
- JavaScript (Node.js): `node bug_snippets/bug2.js` and `node bug_snippets/bug5.js`
- Java: from `bug_snippets/`, run `javac bug3.java && java bug3`  
  
The XSS example requires a browser DOM or a test double to exercise `renderProfile`; running its file with Node.js alone checks that it loads without executing browser code.  

**The snippets are intentionally insecure and must NOT be used in production.**  
