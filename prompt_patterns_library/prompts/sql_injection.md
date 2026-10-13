# SQL Injection Analysis Prompt Template  

**Role**: Security Engineer specialising in database security and secure query design.  
**Task**: Analyse the supplied [LANGUAGE] database-related code to identify queries where untrusted input could alter the intended SQL statement. Assess the use of query construction, parameterisation and relevant database library protections.  
**Input Placeholder**: [DATABASE_CODE], [DATABASE_LIBRARY] and [EXPECTED_QUERY_BEHAVIOUR].  
**Expected Output**: Potential SQL injection points, affected code locations, an explanation of the exploitation risks and safer implementation using parameterised queries or other appropriate protections. If no issues are identified, state that no issues were detected within the scope of the review.  