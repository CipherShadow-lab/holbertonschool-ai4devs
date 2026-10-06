> **NOTE**: All code snippets were passed through Claude, ChatGPT and Gemini for comparison. The best response for each bug is reflected in the logs below.  

# Bug 1 - bug1.py  
**AI Diagnosis**: Gemini: There are two main issues with this code: a syntax error preventing execution and an unhandled edge case that causes a crash at runtime.  
**Suggested Fix**: 1. Add missing parenthesis on the `print()` statement and 2. Add check in case input list is empty (before dividing).  
**Alternative Fixes Tested**: Added check for empty list `if not numbers(): return 0`  
**Result**: Gemini was the only model to identify 2 issues with the code. Both issues were resolved when applying both suggested fixes.  

# Bug 2 - bug2.py
**AI Diagnosis**: Gemini: The issue is a logic error in percentage calculation: `discount_percent` is passed as a whole number (`10`), but the function multiplies directly by `discount_percent` instead of converting it to a decimal (`10 / 100` or `0.10`).  
**Suggested Fix**: Divide `discount_percent` by `100` inside the function.  
**Alternative Fixes Tested**: None    
**Result**: Code fixed by adding the division inside the function (as suggested).  

# Bug 3 - bug3.py
**AI Diagnosis**: Claude: The problem is that `input()` always returns a string, but the code treats the result as a number.  
**Suggested Fix**: Convert the input to an integer when you read it. E.g. `user_age = int(input("Enter your age: "))`    
**Alternative Fixes Tested**: None  
**Result**: Code ran successfully without any errors.  

# Bug 4 - bug4.js
**AI Diagnosis**: Claude: The problem is an off-by-one error in the loop condition, so the last item never gets printed.     
**Suggested Fix**: Use `<=` so the loop includes the last index. Or, more idiomatically, compare against the length directly and drop `lastIndex` altogether.     
**Alternative Fixes Tested**: Tested comparing against the length directly, which was successful.    
**Result**: Both suggested fixes were successful. Also, Claude was the only model to pick up on an issue where the code doesn't generate an error yet prints the incorrect output due to the indexing.  

# Bug 5 - bug5.js
**AI Diagnosis**: Claude: The problem is a logic error in the condition: `hasPermission === false` grants access to people who don't have permission.  
**Suggested Fix**: check for permission being `true` instead of `false`  
**Alternative Fixes Tested**: Comparing a Boolean to true or false was simplified to `return age >= 18 && hasPermissions;` This is because both statements in the line of code are already Boolean expressions. Therefore, to grant access both will need to be `true`  
**Result**: Code successfully tested without any errors.    

# Bug 6 - bug6.sql
**AI Diagnosis**: Text  
**Suggested Fix**: Text  
**Alternative Fixes Tested**: Text  
**Result**: Text  