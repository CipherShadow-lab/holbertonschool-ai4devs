# AI Assistant Configuration

## Objective

Define a reproducible, AI-assisted Visual Studio Code workflow for the representative Python/JavaScript development scenario documented in [`workflow_baseline.md`](workflow_baseline.md). **GitHub Copilot** is the proposed primary IDE-integrated assistant. **ChatGPT** remains an external support tool for explanations, alternative approaches and independent discussion.

## Configuration Files

| File | Purpose | How it is used |
| --- | --- | --- |
| `.copilot-settings.yaml` | Root-level, human-readable project policy covering languages and the code-review workflow | **Reference specification only**; Copilot does not natively load this custom YAML schema |
| `.vscode/settings.json` | Workspace-level VS Code preferences | VS Code reads these settings when the folder is opened as a workspace |
| `.github/copilot-instructions.md` | Repository-wide AI coding guidance | Supported Copilot experiences can apply these repository instructions |
| `.github/prompts/code-review.prompt.md` | Reusable specialised code-review prompt | Open in a compatible VS Code Copilot Chat environment as a prompt file |

The root-level YAML satisfies the assignment's configuration-file requirement without misrepresenting it as a native Copilot configuration format. The `.github` files provide Copilot-specific instructions and a reusable prompt.

## Language-Specific Rules

**Python**
- Use Black-compatible formatting.
- Include type hints for public functions and non-trivial interfaces.
- Prefer explicit error handling and recommend tests for changed behaviour.

**JavaScript**
- Use ESLint-compatible conventions and Prettier formatting.
- Require semicolons and prefer `const` when reassignment is unnecessary.
- Flag unsafe dynamic execution and unvalidated inputs.

The formatting settings reference the VS Code **Black Formatter** (`ms-python.black-formatter`) and **Prettier** (`esbenp.prettier-vscode`) extensions. Python, Pylance and ESLint extensions are also recommended for the reference environment. Formatting and linting tools must be installed separately to function.

## Specialised AI Workflow: Code Review

The reusable prompt at `.github/prompts/code-review.prompt.md` instructs Copilot to examine supplied code or a diff for **security, correctness and maintainability**. Its expected output includes severity, location where known, rationale, a suggested fix and relevant tests. It must distinguish confirmed findings from possibilities and must not invent test results.

**Suggested use:**
1. Open the repository folder in VS Code and install or enable GitHub Copilot and Copilot Chat functionality as required by the installed VS Code version and account.
2. Ensure the required language and formatter extensions are installed.
3. Open Copilot Chat and invoke the `code-review` prompt using the prompt-file functionality available in the installed version, supplying the code or diff to review.
4. Verify each finding manually, apply appropriate changes and run the project's actual tests and linters before committing.

Prompt-file support and invocation details can vary with VS Code and Copilot versions. The files are a proposed configuration and have **not** been validated against a running Copilot installation in this exercise.

## Relationship to Task 0

The baseline identifies context switching, repetitive manual testing and debugging and documentation overhead as potential inefficiencies. Repository instructions and the code-review prompt are designed to reduce manual transfer of code context and standardise review guidance. They do **not** automate test execution or prove improved productivity.

The baseline metrics of 90 minutes per task, 2 hours per bug fix and 15 commits per week are illustrative estimates only. Meaningful impact claims would require timed trials on comparable tasks and recorded results.

## Limitations

This submission documents configuration artifacts for a representative workflow. It does not assert that GitHub Copilot has been installed, that a code review has been executed or that productivity improvements have been measured. The root YAML is explanatory project policy rather than an executable Copilot settings format.
