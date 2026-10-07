## Bug 1 - bug1_fixed.py  
- **Input**: [25, 50, 37, 44, 60]  
- **Expected Output**: 43.2  
- **Actual Output**: 43.2 ✅ (Successful with errors)  

## Bug 2 - bug2_fixed.py  
- **Input**: [("Laptop", 1200), ("Keyboard", 100), ("Mouse", 50)]  
- **Expected Output**: Laptop: 1080, Keyboard: 90, Mouse: 45    
- **Actual Output**: Laptop: 1080, Keyboard: 90, Mouse: 45 ✅ (Successfully ran with correct discount applied)  

## Bug 3 - bug3_fixed.py
- **Input**: 51  
- **Expected Output**: You are an adult. You were born in: 1975  
- **Actual Output**: You are an adult. You were born in: 1975 ✅ (Successfully ran where input string was converted into an integer) 

## Bug 4 - bug4_fixed.js  
- **Input**: ["apples", "bread", "milk", "eggs", "coffee"];  
- **Expected Output**: My shopping List: 1 apples 2 bread 3 milk 4 eggs 5 coffee Total items: 5  
- **Actual Output**: My shopping List: 1 apples 2 bread 3 milk 4 eggs 5 coffee Total items: 5 ✅ (Successfully ran where all indexes were listed) 

## Bug 5 - bug5_fixed.js  
- **Input**: 19
- **Expected Output**: true  
- **Actual Output**: true ✅ (Successfully ran where the correct output of true was shown) 

## Bug 6 - bug6_fixed.sql
- **Input**: <br>SELECT name, age, course<br>
FROM students<br>
WHERE age > 18<br>
  AND course IN ('AI Development' OR course = 'Web Development');<br>  
- **Expected Output**: <br> Alice   | 22  | AI Development<br>
Charlie | 25  | AI Development<br>
- **Actual Output**: <br>Alice   | 22  | AI Development<br>
Charlie | 25  | AI Development<br> ✅ (successfully ran with the correct student output.)