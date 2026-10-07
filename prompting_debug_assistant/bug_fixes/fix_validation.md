## Bug 1 -bug1_fixed.py  
- **Input**: [25, 50, 37, 44, 60]  
- **Expected Output**: 43.2  
- **Actual Output**: 43.2 (Successful with errors) 
- **Notes**: Code was fixed and tested with added parenthesis for `calculate_average` call.    

## Bug 2 -bug2_fixed.py  
- **Input**: [("Laptop", 1200), ("Keyboard", 100), ("Mouse", 50)]  
- **Expected Output**: [("Laptop", 1080), ("Keyboard", 90) ("Mouse", 45)]  
- **Actual Output**: [("Laptop", 1080), ("Keyboard", 90) ("Mouse", 45)]
- **Notes**: Code ran successfully - producing the correct calculations for each product.

## Bug 3 -bug3_fixed.py
- **Input**: 51  
- **Expected Output**: You are an adult. You were born in: 1975  
- **Actual Output**: You are an adult. You were born in: 1975
- **Notes**: Code successfully ran without any errors - due to converting the input (string) into an integer. 

## Bug 4 -bug4_fixed.js  
- **Input**: ["apples", "bread", "milk", "eggs", "coffee"];  
- **Expected Output**: My shopping List: 1 apples 2 bread 3 milk 4 eggs 5 coffee Total items: 5  
- **Actual Output**: My shopping List: 1 apples 2 bread 3 milk 4 eggs 5 coffee Total items: 5
-**Notes**: Code ran successfully, showing all 5 shopping list products. This was fixed by correcting the loop condition - to include all indexes.  

## Bug 5 -bug5_fixed.js  
- **Input**: 19
- **Expected Output**: true  
- **Actual Output**: true
- **Notes**: The correct and expected output of 'true' was displayed due to fixing the code - where both Boolean expressions (studentAge >=18 and hasPermission) were equal to true.  

## Bug 6 -bug6_fixed.sql
- **Input**: <br>SELECT name, age, course<br>
FROM students<br>
WHERE age > 18<br>
  AND (course = 'AI Development' OR course = 'Web Development');<br>  
- **Expected Output**: <br> Alice   | 22  | AI Development<br>
Charlie | 25  | AI Development<br>
- **Actual Output**: <br>Alice   | 22  | AI Development<br>
Charlie | 25  | AI Development<br>