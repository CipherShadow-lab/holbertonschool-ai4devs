# Secrets and Environment Variable Management Prompt Template  

**Role**: Act as a Cloud Security Engineer specialising in secrets management and secure application configuration.  
**Task**: Review how the supplied application stores, retrieves and uses sensitive configuration values, including environment variables and credentials. Identify potential exposure risks, exessive access, insecure defaults and weaknesses in the secrets lifecycle. Do not reproduce secret values in the findings.  
**Input Placeholder**: [CONFIGURATION_CODE], [DEPLOYMENT_SETTINGS] and [SECRET_MANAGEMENT_PRACTICES].   
**Expected Output**: A list of potential weaknesses, affected code or configuration locations, explanation of the risks, recommendations for secure storage and access controls, credential rotation guidance where appropriate and steps for verifying the changes.  