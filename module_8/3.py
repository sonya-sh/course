from peewee import *

conn = SqliteDatabase('db2.sqlite')


class BaseModel(Model):
    class Meta:
        database = conn


class Students(BaseModel):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')


class Courses(BaseModel):
    id = PrimaryKeyField(column_name='id')
    name = CharField(column_name='name')
    time_start = DateTimeField(column_name='time_start')
    time_end = DateTimeField(column_name='time_end')


class Student_Courses(BaseModel):
    student_id = ForeignKeyField(Students, to_field="id", column_name='student_id')
    courses_id = ForeignKeyField(Courses, to_field="id", column_name='courses_id')


def create_tbls():
    Students.create_table()
    Courses.create_table()
    Student_Courses.create_table()

    student = Students(name="Max", surname="Brooks", age=24, city="Spb")
    student.save()
    student = Students(name="John", surname="Stones", age=15, city="Spb")
    student.save()
    student = Students(name="Andy", surname="Wings", age=45, city="Manchester")
    student.save()
    student = Students(name="Kate", surname="Brooks", age=34, city="Spb")
    student.save()

    courses = Courses(name="python", time_start="21.07.2021", time_end="21.08.2021")
    courses.save()
    courses = Courses(name="java", time_start="13.07.2021", time_end="16.08.2021")
    courses.save()

    student_course = Student_Courses(student_id=1, courses_id=1)
    student_course.save()
    student_course = Student_Courses(student_id=2, courses_id=1)
    student_course.save()
    student_course = Student_Courses(student_id=3, courses_id=1)
    student_course.save()
    student_course = Student_Courses(student_id=4, courses_id=2)
    student_course.save()


create_tbls()
for student in Students.select().where(Students.age > 30):
    print(student.name)
print('\n')

query = Students.select().join(Student_Courses).join(Courses).where(Courses.name == 'python')
for student in query:
    print(student.name)
print('\n')

query2 = Students.select().join(Student_Courses).join(Courses).where((Students.city == 'Spb') and (Courses.name == 'python'))
for student in query2:
    print(student.name)


conn.close()
