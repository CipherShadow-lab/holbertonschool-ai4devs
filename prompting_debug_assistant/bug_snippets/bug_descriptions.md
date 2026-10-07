## Bug 1 - bug1.py
**Intended Behaviour**: Prints the average score from an array of numbers (scores).  
**Issue Type**: Syntax Error  
**Notes**: Function fails due to missing parenthesis at calculate_average call.  

## Bug 2 - bug2.py
**Intended Behaviour**: Function calculates discounts of listed products.  
**Issue Type**: Logical Error  
**Notes**: Function recieves an argument for discount_percent that is a whole number (E.g. 10) and fails to convert the number into a decimal percentage.This results in the code calculating 10 times the price - rather than 10% of the price.  

## Bug 3 - bug3.py
**Intended Behaviour**: Function gets user age and calculates their birth year based on the current year.  
**Issue Type**: Runtime Exception  
**Notes**: User input returns a string which is not converted to an integer - when the program calls get_user_age().  

## Bug 4 - bug4.js
**Intended Behaviour**: JavaScript prints the entire shopping list, including the total number of items in the list.  
**Issue Type**: Off-by-One/Loop Error  
**Notes**: There are 5 items in the list however, the loop condition stops before the last item. Causing the result to print only 4 items (not 5).  

## Bug 5 - bug5.js
**Intended Behaviour**: Javascript correctly determines if student has access based on 2 conditions - aged 18 and over and has permission.  
**Issue Type**: Logical Error  
**Notes**: Due to an incorrect boolean condition the JavaScript prints out the wrong output (E.g. True instead of False).    