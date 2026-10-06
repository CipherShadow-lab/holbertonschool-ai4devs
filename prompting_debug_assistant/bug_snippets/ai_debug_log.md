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
**Suggested Fix**: Convert the input to an integer when you read it. E.g. `user_age = int(input("Enter you age: "))`    
**Alternative Fixes Tested**: None  
**Result**: Code worked without any errors.  

# Bug 4 - bug4.py
**AI Diagnosis**: Text  
**Suggested Fix**: Text  
**Alternative Fixes Tested**: Text  
**Result**: Text  

# Bug 5 - bug5.py
**AI Diagnosis**: Text  
**Suggested Fix**: Text  
**Alternative Fixes Tested**: Text  
**Result**: Text  

# Bug 6 - bug6.py
**AI Diagnosis**: Text  
**Suggested Fix**: Text  
**Alternative Fixes Tested**: Text  
**Result**: Text  