> **NOTE** The following are summarised findings for all bug fixes.

## Bug Report - bug1.py
- **Summary**: Syntax error due to missing closing parenthesis.  
- **Root Cause**: Missing closing parenthesis on the print() statement.  
- **Resolution**: Added closing parenthesis to `print(calculate_average(scores))`  
- **Lesson Learned**: Missing closing parenthesis in code will lead to syntax errors - which prevents the code from running. Using an IDE is useful for highlighting and alerting developers where there are mismatches and potenital issues in the code.  

## Bug Report - bug2.py
- **Summary**:  Logic error in calculating the discount (percentage) for listed products.  
- **Root Cause**: The `discount_percent` was being passed as a whole number (10) and multiplied directly with the `price` - instead of being converted to a decimal first.  
- **Resolution**: Corrected the `calculate_discount` function where `discount = price * (discount_percent / 100)`.  
- **Lesson Learned**: In the event of a logic error, a result will still be produced (without errors) but will be wrong. This highlights the importance of conducting tests with known cases (e.g. 10% discount of $100) to catch an error of this type.  

## Bug Report - bug3.py
- **Summary**: TypeError caused by comparing and subtracting strings with integers.  
- **Root Cause**: `input()` in Python always returns a string. When code uses this input for comparison (`if entered_age >= 18:`) Python cannot comapre strings with integers and in turn will generate an error.
- **Resolution**: Converted the received input as an integer - `user_age = int(input("Enter your age: "))` - so the code can correctly perform the required comparison and calculation.  
- **Lesson Learned**: Validate and covert input at the program's boundary - prior to any intended calculations that will be performed in the code.  

## Bug Report - bug4.js
- **Summary**: Off-by-one error in the loop condition, which incorrectly printed the list - not displaying the last item.  
- **Root Cause**: The loop condition `itemIndex < lastIndex` stopped before reaching index 4. This is because `const lastIndex = shoppingList.length - 1;`  
- **Resolution**: Changed the code to loop directly against `shoppingList.length` - without creating a `lastIndex` variable.  
- **Lesson Learned**: In JavaScript, use an array's `.length` as the loop's boundary rather than calculating and storing the last index in a variable.  

## Bug Report - bug5.js
- **Summary**: Logical error in the condition: `hasPermission === false` which grants access to students who don't have permission.  
- **Root Cause**: Using the `||` operator meant that access was granted if the student is 18 or older OR `hasPermission` is `false`. The intended rule is the student can access the course if they are 18 or older AND they have permission. 
- **Resolution**: In the`canAccessCourse` function, the Boolean value for `hasPermission` was changed to equal `true`. Also the `||` operator was changed to `&&` to ensure both conditions are true for access to be granted.
- **Lesson Learned**: The desired rule needs to be translated into logic carefully. Testing (using multiple test cases) is imperative to ensure that the correct logic is being applied and executed.  
