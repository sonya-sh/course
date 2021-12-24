from peewee import *

conn = SqliteDatabase('studydb3.sqlite')


class BaseModel(Model):
    class Meta:
        database = conn


class Students(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    surname = CharField()
    age = IntegerField()
    city = CharField()


class Courses(BaseModel):
    id = PrimaryKeyField()
    name = CharField()
    time_start = DateTimeField()
    time_end = DateTimeField()


class Student_Courses(BaseModel):
    student_id = ForeignKeyField(Students, to_field="id")
    courses_id = ForeignKeyField(Courses, to_field="id")


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

    st_c = Student_Courses(student_id=1, courses_id=1)
    st_c.save()
    st_c = Student_Courses(student_id=2, courses_id=1)
    st_c.save()
    st_c = Student_Courses(student_id=3, courses_id=1)
    st_c.save()
    st_c = Student_Courses(student_id=4, courses_id=2)
    st_c.save()


#create_tbls()
for student in Students.select().where(Students.age > 30):
    print(student.name, student.age)
print('\n')

query = Students.select().join(Student_Courses).join(Courses).where(Courses.name == 'python')
for student in query:
    print(student.name, student.city)
print('\n')

query2 = Students.select().join(Student_Courses).join(Courses).where((Students.city == 'Spb') & (Courses.name == 'python'))
for st in query2:
    print(st.name)

conn.close()
