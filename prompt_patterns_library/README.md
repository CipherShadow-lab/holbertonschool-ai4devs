![prompt-engineering-ai](Images/ai.jpg)  
<br>

# AI Prompt Engineering for Secure Software Development  

## Overview  

This project explores how AI prompt engineering can support secure software development workflows, with a focus on code quality, vulnerability detection, security testing, documentation and configuration management.  
  
The project contains a reusable library of prompt templates designed to help developers use AI tools more effectively when reviewing code, identifying potential security weaknesses, generating tests and producing technical documentation.  
  
Each template defines a specific role, task, required inputs and expected output. This structure promotes consistency, clarity and reusability across different development and cybersecurity scenarios.  
  
  
## Objectives  
  
- Develop reusable AI prompt templates for common software development and cybersecurity tasks.  
- Apply structured prompt engineering techniques to improve the relevance and consistency of AI-generated responses.  
- Support secure coding practices and vulnerability identification.  
- Assist with automated security test design and regression prevention.  
- Improve the quality and consistency of technical and security documentation.  
- Establish a standardised prompt library that can be extended as new use cases emerge.  
  
  
## Project Structure  
  
The prompt templates are organised in the `prompts/` directory, with one Markdown file per use case.  
  
```
prompts/
├── refactoring.md
├── input-validation.md
├── hardcoded-secrets.md
├── sql-injection.md
├── xss-analysis.md
├── authentication-authorisation.md
├── negative-input-testing.md
├── access-control-testing.md
├── regression-security-testing.md
├── secure-api-documentation.md
├── threat-modelling.md
├── security-review-reporting.md
├── dependency-vulnerability-review.md
├── secure-configuration-review.md
└── secrets-environment-management.md
```  
  

## Prompt Template Structure  
  
Every template follows a consistent Markdown structure to make prompts easier to understand, reuse and maintain.  
  
**Role:**  
Defines the expertise and perspective the AI should adopt.  
  
**Task:**  
Describes the task, its scope, and relevant constraints.  
  
**Input Placeholder:**  
Identifies the information required to perform the task.  
  
**Expected Output:**  
Specifies the deliverables and their structure.  
  
> [!NOTE]
> Templates use descriptive placeholders in uppercase SNAKE_CASE, such as `[SOURCE_CODE]`, `[LANGUAGE]`, `[SECURITY_REQUIREMENTS]`, and `[TESTING_FRAMEWORK]`.  
  
These placeholders can be replaced with project-specific information when a template is used.  
  
  
## Use Cases  
  
### 1. Secure Code Quality  
- **Secure Refactoring**: Improve readability, maintainability and performance while preserving functionality and security requirements.  
- **Input Validation and Sanitisation**: Identify weaknesses in the handling of untrusted input and recommend appropriate validation rules.  
- **Hardcoded Secrets Detection**: Identify potential exposed credentials and recommend secure remediation without reproducing secret values.  
  
### 2. Vulnerability Detection and Debugging  
- **SQL Injection Analysis**: Identify unsafe database query construction and recommend parameterised queries or other appropriate protections.  
- **Cross-Site Scripting (XSS) Analysis**: Review the handling and rendering of untrusted content to identify potential XSS vulnerabilities.  
- **Authentication and Authorisation Review**: Identify weaknesses in identity verification, session management, permissions and access control.  
  
### 3. Security Testing  
- **Negative Input Validation Testing**: Generate automated tests for malformed, unexpected and invalid input.  
- **Access Control Testing**: Verify that users can access resources and perform actions only when authorised.  
- **Security Regression Testing**: Generate tests to verify that previously fixed security vulnerabilities are not reintroduced.  
  
### 4. Security Documentation  
- **Secure API Documentation**: Produce developer-facing API documentation covering authentication, permissions, validation and error handling.
- **Threat Modelling**: Identify important assets, trust boundaries, potential attackers, threats and recommended mitigations.  
- **Security Review Reporting**: Convert security review findings into structured reports with evidence, impact, remediation and verification steps.  
  
### 5. Dependency and Configuration Security  
- **Dependency Vulnerability Review**: Assess dependency manifests, package versions, and vulnerability scan results to identify issues requiring investigation.  
- **Secure Configuration Review**: Identify potentially insecure application and deployment settings.  
- **Secrets and Environment Variable Management**: Review how sensitive configuration values are stored, accessed, protected, and rotated.  
  
## How to Use the Templates  

1. Navigate to the `prompts/` directory.  
  
2. Select the Markdown file corresponding to the task you want to perform.  
  
3. Read the template's role, task, input requirements and expected output.  
  
4. Replace the placeholders with relevant project information.  
  
5. Provide the completed prompt to your preferred AI tool.  
  
6. Review the generated response, verify important claims and test any proposed code changes before adopting them.  
  
  
### Example  
  
The following example demonstrates how the secure refactoring template can be adapted for a Python function.  
  
```
# Secure Refactoring Prompt

Role: Senior Software Engineer specialising in secure
coding, maintainability and software design patterns.

Task: Refactor the supplied Python code to improve
readability and maintainability without changing its
intended behaviour or introducing security weaknesses.

Input Placeholder:
- SOURCE_CODE: [Insert Python function]
- LANGUAGE: Python
- EXISTING_TESTS: [Insert relevant unit tests]
- SECURITY_REQUIREMENTS: Preserve input validation and
  existing access control checks.

Expected Output:
Refactored source code, an explanation of the changes,
relevant design pattern references where applicable,
and any potential security concerns.
```  
  

The example illustrates how a reusable template can be populated with specific requirements before being submitted to an AI tool.  

  
## Security Considerations
  
AI-generated code, tests, documentation and security findings should be treated as recommendations that require verification.  
  
- Do NOT submit real passwords, API keys, access tokens, private keys or other sensitive credentials to AI tools unless the environment and its data-handling policies explicitly permit it. 
   
- Remove or redact sensitive values before sharing source code and configuration files.  

- Verify potential vulnerabilities against the actual implementation and relevant security references.  
  
- Run generated tests and review proposed code changes before integrating them into a project.  
  
- Confirm dependency vulnerability information using authoritative sources and current package information.  
  
- Do not rely on AI-generated security assessments as a substitute for appropriate security testing and expert review.  

  
## Limitations  
  
AI-generated results may contain incorrect assumptions, incomplete findings, outdated information or recommendations that do not suit the application's architecture.  
  
The quality of the output depends on the clarity of the prompt, the completeness of the supplied information and the capabilities of the selected AI tool.  
  
The templates are intended to support developer productivity and security review as opposed to replacing established development practices, automated security tools or professional security assessments.  
  
  
## Project Status  
  
The prompt library contains 15 reusable Markdown templates covering the identified software development and cybersecurity use cases.  
  
The templates follow a standardised structure and placeholder naming convention and have passed the project's checker.  
  
  
## Future Improvements  

Potential future enhancements include:  
  
- Adding language-specific examples for Python, JavaScript and other programming languages.  
  
- Introducing templates for additional security testing and code review scenarios.  
  
- Developing example inputs and outputs for each prompt.  
  
- Evaluating prompt effectiveness using representative code samples and test cases.  
  
- Integrating selected prompts into development workflows and continuous integration pipelines.  
  
- Refining templates based on testing results and developer feedback.  
  
  
## Conclusion  
  
This project demonstrates how structured prompt engineering can be applied to secure software development.  
  
By defining clear roles, tasks, inputs and outputs, the prompt library provides a reusable foundation for AI-assisted coding, debugging, testing, documentation and cybersecurity analysis.  
  
The emphasis is on using AI as a development aid while maintaining human oversight, validating results and applying established security practices.  