<p align="center">
  <img
    src="/Images/FAULTLINE-APIPROTOTYPING.png"
    alt="FAULT//INE — ATTACK CHAINS DECODED"
    width="100%"
  />
</p>
<br>
  
## Purpose  
  
FAULT//INE is a developer-focused application security concept that aims to help users understand potential vulnerabilities in source code, how those weaknesses may relate and how they could contribute to attack paths. This part of the project establishes an initial API contract supporting that workflow and is **not** a claim that a production-grade scanner or exploit-validation engine has been implemented.

**The API design is documented in two stages**:   
  
- `api_requirements.md` defines the intended behaviour and constraints 
- `api_specification.yaml` and `api_specification.json` will express the same interface in OpenAPI 3.0 format.
<br>

## Target Users  

**Primary users**: Software developers who need to identify, understand and remediate potential vulnerabilities in their application source code.   
  
**Supporting users**: Security professionals who may assist with reviewing findings, interpreting potential attack chains and advising on remediation when additional expertise is needed.  
<br>
  
## Agreed MVP Scope  

The FAULT//INE API prototype focuses on defining a structured, secure interface for managing source-code projects, initiating vulnerability scans, and retrieving findings and potential attack-chain data.  
<br>  
| Capability | Agreed MVP Scope |
|---|---|
| Target Users | Primarily software developers, with security professionals providing additional support and expertise when required. |
| Source-Code Language | Python (`.py`) files only. |
| File Uploads | Individual file selection and upload, with multiple files supported per project. |
| File Validation | Maximum 5 MB per file; empty files and unsupported file types are rejected. |
| Project Management | Create, retrieve, update, and delete projects. |
| Scan Management | Initiate scans and retrieve scan status and results. |
| Vulnerability Findings | Retrieve identified security weaknesses, including severity, location, description, and remediation guidance. |
| Attack-Chain Analysis | Retrieve potential attack sequences and relationships between findings. |
| Node Map Visualisation | Provide structured data for the frontend to display relationships between vulnerabilities. |
| Attack Chain View | Provide sequential attack-path information, including prerequisites, potential impact, and remediation guidance. |
| API Security | JWT-based authentication, input validation, and consistent error responses. |
| API Documentation | OpenAPI 3.0 specification maintained in YAML and JSON formats. |
  
**Agreed upload validation**: Accept `.py` files only; reject empty files; enforce a maximum of 5 MB per file. Treat uploaded code as untrusted data and do not execute it during ingestion. File-size limits are prototype constraints, not a statement about all future versions.  
<br>
  
## Scope Exclusions  

The following capabilities are intentionally excluded from the initial API prototype to maintain a focused, achievable MVP.  
<br>
| Excluded Capability | Rationale |
|---|---|
| GitHub repository integration | Keeps source-code ingestion limited to local file uploads. |
| Folder and bulk uploads | Reduces ingestion and validation complexity. |
| Multi-language analysis | Limits initial analysis to Python source files. |
| Live infrastructure and firewall scanning | Keeps analysis focused on application source code rather than deployed environments. |
| Automated exploitation | Focuses on identifying and visualising potential attack chains, not executing attacks. |
| CI/CD integration | Avoids introducing pipeline dependencies during API prototyping. |
| Production-grade AI analysis | Keeps the prototype focused on API design rather than implementing a complete detection engine. |  
<br>

## Design Rationale  

The Node Map is an interactive visualisation of findings and their potential relationships, rather than a separate CRUD resource. The Attack Chain view explains selected potential exploitation sequences step by step. A relationship between findings does not by itself establish an exploitable chain; generated scenarios must be labelled as potential and subject to validation.

Projects are suitable for conventional CRUD operations. Scanner-produced findings should not be freely created or rewritten as if they were user-authored records. Authentication, pagination and error handling will be defined consistently across the requirements - and OpenAPI specification.

**Details to finalise during requirements and API design**:  
  
The backend framework, precise endpoint paths and schemas, supported scan/detection patterns, JWT issuance and expiry, rate-limit policy, latency targets, source-code retention and deletion rules, and whether analysis uses mock results or an integrated scanner have not yet been agreed. These must be decided explicitly before the corresponding specification details are finalised.  
<br>
  
## Deliverables  

- README.md — scope, exclusions, and design rationale (this document).
- api_requirements.md — Task 0: API requirements.
- api_specification.yaml — Task 1: OpenAPI 3.0 definition.
- api_specification.json — equivalent OpenAPI 3.0 definition in JSON.  
<br>

*This README is supplementary coursework documentation and should be updated if later design decisions change the agreed scope.*