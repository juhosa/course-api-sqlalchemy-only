# CourseAPI ORM only

CourseAPIn tietokantaan liittyvät toiminnallisuudet yhdessä paketissa, ilman FastAPIa ja muita.

Pelkästään SQLAlchemy.

## Käyttö

Luo virtualenv ja asenna paketit

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Testaa scriptiä python REPLissä (eli venv aktiivisena suorita `python`).

```
>>> from main import Teacher, session, save, create_all, Student, Course, StudentGrades
>>> create_all() # luo tietokannan
>>> ope1 = Teacher(name='Ope 1')
>>> save(ope1)
>>> kurssi1 = Course(name='Kurssi 1', credits=3, teacher=ope1)
>>> save(kurssi1)
>>> opiskelija1 = Student(name='Ossi Opiskelija')
>>> save(opiskelija1)
>>> opiskelija1.courses
[]
>>> kurssi1.students.append(opiskelija1)
>>> save(kurssi1)
>>> kurssi1.students
[<main.Student object at 0x10a1b4be0>]
>>> kurssi1.students[0].name
'Ossi Opiskelija'
>>> opiskelija1.courses
[<main.Course object at 0x10b608790>]
>>> opiskelija1.courses[0].name
'Kurssi 1'
>>> opiskelija1.courses[0].credits
3
>>> o1_grade = StudentGrades(student=opiskelija1, course=kurssi1, grade=4)
>>> save(o1_grade)
>>> opiskelija1.grades
[<main.StudentGrades object at 0x10b79ff10>]
>>> [{g.course.name: g.grade} for g in opiskelija1.grades]
[{'Kurssi 1': 4}]
```
