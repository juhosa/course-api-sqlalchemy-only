from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm.session import Session

# echo = True tulostaa ORMin generoimat SQL-lauseet
engine = create_engine('sqlite:///course_api_orm_only.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine)


def save(o):
    session.add(o)
    session.commit()


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # courses = db.relationship('Course', backref='teacher')
    # kun käyttää back_populates, pitää suhde määrittää kummassakin mallissa.
    # backreffillä riittää vaan toisessa
    courses = relationship('Course', back_populates='teacher')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    credits = Column(Integer)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship('Teacher', back_populates='courses')

    students = relationship(
        'Student', secondary='student_course_linker', back_populates='courses')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    courses = relationship(
        'Course', secondary='student_course_linker', back_populates='students')

    grades = relationship('StudentGrades')


class StudentCourseLink(Base):
    __tablename__ = 'student_course_linker'

    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)


class StudentGrades(Base):
    __tablename__ = 'students_grades'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    grade = Column(Integer, nullable=False)
    student = relationship('Student', back_populates='grades')
    course = relationship('Course')
