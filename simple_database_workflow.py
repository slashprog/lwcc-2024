# The queries we are going to use:

DSN = "school"

CREATE_STUDENTS = """
    CREATE TABLE IF NOT EXISTS students(
        name    VARCHAR(32) NOT NULL,
        grade   INTEGER NOT NULL,
        score   INTEGER
    )
"""

INSERT_STUDENT = """
    INSERT INTO students(name, grade) VALUES(?,?)
"""

SELECT_STUDENTS = """
    SELECT * FROM students
"""

import sqlite3 as driver

with driver.connect(DSN) as conn:
    cursor = conn.cursor()
    cursor.execute(CREATE_STUDENTS)
    
    while True:
        name = input("Enter student name (or 'exit' to stop): ")
        if name == "exit":
            break
        grade = int(input("Enter grade: "))
        score = int(input("Enter score: "))

        cursor.execute(INSERT_STUDENT, (name, grade, score))

    cursor.execute(SELECT_STUDENTS)
    for name, grade, score in cursor:
        print(f"Name: {name}, Grade: {grade}, Score: {score}")
   