# Prompt Use Cases

This document categorises common use cases for AI-assisted secure software development. Each use case defines a goal, the required input and the expected output to support reusable prompt engineering in coding workflows.

## Secure Code Quality  
- **Secure Refactoring**  
  - **Goal**: Improve code readabilty, maintainability and performance without introducing new security weaknesses.  
  - **Input**: Source code written in [LANGUAGE], existing tests and relevant security requirements.  
  - **Output**: Improved code, explanation of the changes and potential security improvements or concerns.  

- **Input Validation and Sanitisation**  
  - **Goal**: Identify weaknesses in how an application handles user input, which could lead to injection attacks.  
  - **Input**: [CODE], expected input formats and applicable validation rules.  
  - **Output**: Potential input-handling vulnerabilities, recommended validation rules and examples of safe code.  

- **Hardcoded Secrets Detection**  
  - **Goal**: Identify hardcoded passwords, API keys, tokens and other sensitive credentials in source code.  
  - **Input**: [CODE] and relevant secret-management requirements.  
  - **Output**: Potential locations of exposed secrets, explanation of the risks and recommendations for secure storage and credential rotation. Secret values should not be repeated in the report.  

## Vulnerability Detection and Debugging
- **SQL Injection Analysis**  
  - **Goal**: Identify database queries that may allow untrusted input to change the intended SQL statement. 
  - **Input**: [DATABASE_CODE], [LANGUAGE] and the database library or framework in use.  
  - **Output**: Potential injection points, explanation of the risks and safer implementations using parameterised queries where appropriate.  

- **Cross-site Scripting (XSS) Analysis**  
  - **Goal**: Identify areas of the web application where untrusted content could be interpreted as executable script in the user's browser.  
  - **Input**: [WEB_CODE], the rendering context and frontend framework.  
  - **Output**: Potential XSS vulnerabilities, affected code locations and recommendations for context-appropriate output encoding or sanitisation.  

- **Authentication and Authorisation Review**  
  - **Goal**: Identify weaknesses in user authentication, session management and access permissions that could allow unauthorised access.  
  - **Input**: [AUTHENTICATION_CODE], user roles and the application's access control requirements.  
  - **Output**: Potential security flaws, explanations of unauthorised access risks and recommended fixes.  

## Security Testing  
- **Negative Input Validation Testing**  
  - **Goal**: Verify that the application safely handles malformed, unexpected or malicious input.  
  - **Input**: [FUNCTION_OR_ENDPOINT], accepted input rules and the testing framework.  
  - **Output**: Automated test cases covering invalid input, boundary conditions and expected error handling.  

- **Access Control Testing**  
  - **Goal**: Ensure users can only access resources and perform actions permitted by their assigned roles and permissions.  
  - **Input**: [API_ENDPOINTS], user roles, resource ownership rules and testing guidelines.  
  - **Output**: Rewritten code with consistent style  

- **Testing Previously Fixed Security Problems**
  - **Goal**: Ensure a previous security issue is not re-introduced following future code changes.  
  - **Input**: [FIXED_VULNERABILITY], updated code and existing tests.  
  - **Output**: Automated tests that verify that the fix remains effective, along with expected results and recommendations for integrating tests into continuous integration.  

## Security Documentation  
- **Secure API Documentation**  
  - **Goal**: Document how developers should securely interact with an API, including its authentication, authorisation and input validation requirements.  
  - **Input**: [API_SPECIFICATION], authentication methods, access control rules and request validation requirements.  
  - **Output**: Structured API documentation covering security requirements, expected error responses and safe usage examples.  

- **Threat Modelling**  
  - **Goal**: Identify important assets, potential attackers and possible attack paths before they become actual security incidents.  
  - **Input**: [SYSTEM_ARCHITECTURE], data flows, sensitive assets, trust boundaries and relevant assumptions about potential attackers.  
  - **Output**: A threat summary identifying potential attacks, their likely impact and recommended mitigations.  

- **Security Review Reporting**
  - **Goal**: Present security review findings in a clear and consistent format that helps developers to understand and resolve identified problems.  
  - **Input**: [CODE_REVIEW_FINDINGS], affected components, supporting evidence and applicable security requirements.  
  - **Output**: A structured report containing findings, severity estimates, potential impact, remediation steps and recommended verification tests.  

## Dependency and Configuration Security  
- **Dependency Vulnerability Review**  
  - **Goal**: Identify third-party packages that may contain known security vulnerabilities or require security updates.  
  - **Input**: [DEPENDENCY_MANIFEST], package versions and available vulnerability scan results.  
  - **Output**: A list of potentially vulnerable packages and recommendations for security updates.  

- **Secure Configuration Review**  
  - **Goal**: Identify application settings that could weaken security such as overly permissive access or disabled security protections.  
  - **Input**: [CONFIGURATION_FILES], deployment environment details and security requirements.  
  - **Output**: Potentially insecure settings, explanation of their risks and recommendations for safer configurations.  

- **Secrets and Environment Variable Management**
  - **Goal**: Review how an application stores and accesses sensitive configuration values to reduce the risk of credential exposure.  
  - **Input**: [CONFIGURATION_CODE], deployment settings and existing secret-management practices.  
  - **Output**: Potential weaknesses in secret handling recommendations for secure storage and access - and steps for verifying the changes. 