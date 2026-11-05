# GitHub Copilot Productivity Sprint — Environment Setup

## 1. Objective

Prepare and verify a development environment using Visual Studio Code and GitHub Copilot for a controlled productivity comparison between manual and AI-assisted coding workflows.

## 2. Development Environment

| Component | Version / Configuration |
|---|---|
| Operating System | Windows x64 (Build 10.0.26300) |
| IDE | Visual Studio Code 1.144.1 (User Setup) |
| Node.js Runtime (VS Code) | 24.22.1 |
| AI Coding Assistant | GitHub Copilot |
| Integrated Copilot Component | 1.0.103 |
| Integrated Copilot SDK | 1.0.27 |

### Relevant VS Code Extensions

| Extension | Version |
|---|---|
| Python (`ms-python.python`) | 2026.10.0 |
| Pylance (`ms-python.vscode-pylance`) | 2026.4.1 |
| Python Debugger (`ms-python.debugpy`) | 2026.6.0 |
| Pylint (`ms-python.pylint`) | 2026.6.0 |

The GitHub Copilot extension was not listed by the VS Code extension-management CLI. However, Copilot components were present in the IDE, and Copilot Chat functionality was successfully verified.

## 3. GitHub Copilot Setup

### Standard Setup Procedure

1. Install or launch Visual Studio Code.
2. Open the Extensions panel using `Ctrl + Shift + X`.
3. Search for GitHub Copilot, published by GitHub, and install or enable it if required.
4. Open Copilot Chat or select the available Copilot setup option.
5. Sign in with a GitHub account that has access to Copilot.
6. Complete any required authorisation steps.
7. Verify functionality by submitting a simple coding prompt.

### Actual Environment Configuration

Visual Studio Code and Copilot components were already present before this task.

The Copilot extension interface initially displayed a message indicating that it was disabled globally. However, subsequent testing confirmed that Copilot Chat was operational.

The command below was used to inspect installed extensions:

```powershell
code --list-extensions --show-versions
```

No standalone GitHub Copilot extension appeared in the resulting list. No reinstall was necessary to complete functional verification.

## 4. Configuration Verification

Copilot Chat was tested directly inside Visual Studio Code.

**Test Prompt:**

```text
Write a Python function that returns the square of a number.
```

**Generated Response:**

```python
def square(number):
    return number ** 2
```

**Result:** Successful.

Copilot generated a syntactically valid Python function that implements the requested operation.

This confirms that Copilot Chat can respond to coding prompts within the configured IDE. Inline code-completion functionality was not separately tested.

## 5. Manual and AI-Assisted Workflow Preparation

The productivity sprint will compare equivalent programming tasks under two conditions:

- **Manual Workflow:** Complete tasks without AI-generated code or suggestions.
- **AI-Assisted Workflow:** Complete tasks with GitHub Copilot enabled.

The same IDE, programming language, task requirements and testing approach should be maintained across both conditions where possible.

Before manual runs, Copilot assistance should be disabled and verified as inactive. It can then be re-enabled for AI-assisted runs.

Task completion times, code quality and other required productivity metrics will be recorded during the experiment, not during environment setup.

## 6. References

- [Visual Studio Code — Set Up GitHub Copilot](https://code.visualstudio.com/docs/setup/copilot)
- [Visual Studio Code — Extension Management](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
- [GitHub Docs — GitHub Copilot](https://docs.github.com/en/copilot)

## 7. Setup Status

**Status:** Completed — Copilot Chat successfully verified.

The development environment is prepared for the AI-assisted coding portion of the productivity sprint. The manual workflow and benchmark measurements will be verified and completed during subsequent tasks.
