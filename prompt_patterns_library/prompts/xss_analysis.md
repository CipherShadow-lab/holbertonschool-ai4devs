# Cross-site Scripting (XSS) Analysis Prompt Template  

**Role**: Act as a Web Application Security Engineer speciaising in browser security and cross-site scripting prevention.  
**Task**: Analyse the supplied [LANGUAGE] web application code to identify places where untrusted content could be interpreted as executable script in a user's browser. Consider the rendering context, framework protections and any unsafe HTML insertion or DOM manipulation.  
**Input Placeholder**: [WEB_CODE], [RENDERING_CONTEXT] and [FRONTEND_FRAMEWORK].  
**Expected Output**: Potential XSS vulnerabilities, affected code locations, relevant execution context, explanation of the risks and recommendations for context-appropriate ouput encoding, sanitisation or safer rendering methods. If no issues are identified, state that no issues were detected within the scope of the review.  