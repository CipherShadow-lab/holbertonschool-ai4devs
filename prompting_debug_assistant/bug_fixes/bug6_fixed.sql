CREATE TABLE students (
    id INTEGER,
    name VARCHAR(50),
    age INTEGER,
    course VARCHAR(50)
);

INSERT INTO students VALUES
    (1, 'Alice', 22, 'AI Development'),
    (2, 'Ben', 17, 'Web Development'),
    (3, 'Charlie', 25, 'AI Development'),
    (4, 'Diana', 19, 'Cyber Security');

SELECT name, age, course
FROM students
WHERE age > 18
AND (course = 'AI Development' OR course = 'Web Development');
