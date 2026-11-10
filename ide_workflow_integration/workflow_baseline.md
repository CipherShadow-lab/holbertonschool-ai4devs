# Workflow Baseline

## Baseline Context

This document establishes a **representative productivity baseline** for a Python/JavaScript development workflow using Visual Studio Code. It outlines the development environment, identifies common workflow inefficiencies and defines illustrative productivity metrics to support the evaluation of AI-assisted IDE integration. The scenario components and figures are **assumptions**, not verified installations or historical measurements.

## Current IDE Setup

- **Editor:** Visual Studio Code (VS Code), using a current stable release; no specific version is assumed.
- **External AI support:** ChatGPT, accessed separately from the IDE for explanations, troubleshooting and development guidance (reference workflow).
- **Representative development languages:** Python and JavaScript.
- **Representative editor extensions:** Microsoft Python, Pylance, ESLint and Prettier (reference scenario; installation not verified).
- **Representative developer tools:** VS Code integrated terminal, Git and GitHub (reference scenario; installation not verified).
- **Typical reference workflow:** Read a task, edit code in VS Code, consult external documentation or ChatGPT, run checks manually in the terminal, review changes and commit through Git.
- **IDE-integrated AI assistant:** Not part of the baseline. GitHub Copilot is the **planned primary assistant** for Task 1.

## Pain Points

1. **Context switching:** Moving between VS Code, documentation and external AI support requires copying code and error messages between tools, interrupting development flow.
2. **Manual testing and debugging:** Re-running checks, interpreting failures and tracing errors without a streamlined automated workflow increases turnaround time.
3. **Repetitive documentation:** Updating README files, comments and developer notes manually can consume time and create inconsistencies with code changes.

## Productivity Metrics

The following figures are **illustrative starting estimates for the reference scenario**, not measured results or industry benchmarks. They provide comparison targets for a future controlled evaluation.

| Metric | Illustrative Baseline | Measurement Method for Future Validation |
| --- | --- | --- |
| Average task completion time | 90 minutes per comparable development task | Time from starting a defined task to meeting its acceptance criteria; average across multiple tasks. |
| Bug fix turnaround | 2 hours per resolved bug | Time from reproducing a defect to verifying a fix; average across comparable bugs. |
| Weekly Git commits | 15 commits per week | Count commits authored during a consistent seven-day period using Git history. |

## Baseline Limitations

This is a **documented reference scenario**, not an audited record of an existing developer environment. Estimates must not be presented as observed productivity data. Any later claim of improvement would require comparable tasks, consistent measurement methods and actual post-integration results.
