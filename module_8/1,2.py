import sqlite3

conn = sqlite3.connect('db1.sqlite')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY, name varchar(32), surname varchar(32), age integer, city varchar(32))")
cursor.execute("CREATE TABLE IF NOT EXISTS Courses (id INTEGER PRIMARY KEY, name varchar(32), time_start varchar(32), time_end varchar(32))")

cursor.executemany("INSERT INTO Students (id, name, surname, age, city) VALUES (?, ?, ?, ?, ?)", [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany("INSERT INTO Courses (id, name, time_start, time_end) VALUES (?, ?, ?, ?)", [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')])

cursor.execute("CREATE TABLE IF NOT EXISTS Student_Courses (student_id integer, courses_id integer, FOREIGN KEY(student_id) REFERENCES Students(id), FOREIGN KEY(courses_id) REFERENCES Courses(id))")
cursor.executemany("INSERT INTO Student_Courses (student_id, courses_id) VALUES (?, ?)", [(1, 1), (2, 1), (3, 1), (4, 2)])

conn.commit()

students_30 = cursor.execute("SELECT name, age FROM Students WHERE age > 30").fetchall()
students_python = cursor.execute("""SELECT Students.name, Courses.name 
                                    FROM 
                                    Students, Courses, Student_Courses 
                                    WHERE 
                                    (courses_id = Courses.id = 1) and (student_id = Students.id)""").fetchall()
students_python_spb = cursor.execute("""SELECT Students.name, Courses.name, Students.city 
                                   FROM 
                                   Students, Courses, Student_Courses 
                                   WHERE
                                   (courses_id = Courses.id = 1) and (student_id = Students.id) and (Students.city = 'Spb')""").fetchall()
print(students_30)
print(students_python)
print(students_python_spb)

conn.close()

