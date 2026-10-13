# Cross-site Scripting (XSS) Analysis Prompt Template  

**Role**: Web Application Security Engineer specialising in browser security and cross-site scripting prevention.  
**Task**: Analyse the supplied source code to identify locations where untrusted content could be interpreted as executable script in a user's browser. Consider the rendering context, framework protections and unsafe HTML insertion or DOM manipulation.  
**Input Placeholder**: [SOURCE_CODE], [LANGUAGE], [FRONTEND_FRAMEWORK] and [SECURITY_REQUIREMENTS].  
**Expected Output**: Potential XSS vulnerabilities, affected code locations, relevant execution context, explanation of the risks and recommendations for context-appropriate output encoding, sanitisation or safer rendering methods. If no issues are identified, state that no issues were detected within the scope of the review.  