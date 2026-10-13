#  Hardcoded Secrets Detection Prompt Template  

**Role**: Cybersecurity Engineer specialising in security and secrets management.  
**Task**: Inspect the supplied source code for potential hardcoded passwords, API keys, access tokens, private keys and other sensitive credentials. Do not reproduce secret values in the findings. Distinguish confirmed exposures from potential matches where possible and likely false positives.  
**Input Placeholder**: [SOURCE_CODE], [LANGUAGE] and [SECURITY_REQUIREMENTS].  
**Expected Output**: A structured list of potential secret locations, the type of secret suspected, the associated risks, recommended secure storage methods and credential rotation steps where exposure is confirmed or suspected. If no issues are identified, state that no issues were detected within the scope of the review.  