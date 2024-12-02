from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = "Student"
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    com_method = Column(String, nullable=False)
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__ = "Teacher"
    teacher_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    com_method = Column(String, nullable=False)
    exams = relationship("Exam", back_populates="teacher")

class Exam(Base):
    __tablename__ = "Exam"
    exam_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    teacher_id = Column(Integer, ForeignKey("Teacher.teacher_id"), nullable=False)
    teacher = relationship("Teacher", back_populates="exams")
    grades = relationship("Grade", back_populates="exam")

class Grade(Base):
    __tablename__ = "Grade"
    student_id = Column(Integer, ForeignKey("Student.student_id"), primary_key=True)
    exam_id = Column(Integer, ForeignKey("Exam.exam_id"), primary_key=True)
    grade_value = Column(Integer, nullable=False)
    student = relationship("Student", back_populates="grades")
    exam = relationship("Exam", back_populates="grades")

class Model:
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:1234@localhost/postgres")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_student(self, student_id, first_name, last_name, com_method):
        session = self.Session()
        student = Student(student_id=student_id, first_name=first_name, last_name=last_name, com_method=com_method)
        session.add(student)
        session.commit()
        session.close()

    def get_all_students(self):
        session = self.Session()
        students = session.query(Student).all()
        session.close()
        return students

    def update_student(self, student_id, column, new_value):
        session = self.Session()
        student = session.query(Student).get(student_id)
        if student:
            setattr(student, column, new_value)
            session.commit()
        session.close()

    def delete_student(self, student_id):
        session = self.Session()
        student = session.query(Student).get(student_id)
        if student:
            session.delete(student)
            session.commit()
        session.close()

    def add_teacher(self, teacher_id, first_name, last_name, com_method):
        session = self.Session()
        teacher = Teacher(teacher_id=teacher_id, first_name=first_name, last_name=last_name, com_method=com_method)
        session.add(teacher)
        session.commit()
        session.close()

    def get_all_teachers(self):
        session = self.Session()
        teachers = session.query(Teacher).all()
        session.close()
        return teachers

    def update_teacher(self, teacher_id, column, new_value):
        session = self.Session()
        teacher = session.query(Teacher).get(teacher_id)
        if teacher:
            setattr(teacher, column, new_value)
            session.commit()
        session.close()

    def delete_teacher(self, teacher_id):
        session = self.Session()
        teacher = session.query(Teacher).get(teacher_id)
        if teacher:
            session.delete(teacher)
            session.commit()
        session.close()

    def add_exam(self, exam_id, date, teacher_id):
        session = self.Session()
        exam = Exam(exam_id=exam_id, date=date, teacher_id=teacher_id)
        session.add(exam)
        session.commit()
        session.close()

    def get_all_exams(self):
        session = self.Session()
        exams = session.query(Exam).all()
        session.close()
        return exams

    def update_exam(self, exam_id, column, new_value):
        session = self.Session()
        exam = session.query(Exam).get(exam_id)
        if exam:
            setattr(exam, column, new_value)
            session.commit()
        session.close()

    def delete_exam(self, exam_id):
        session = self.Session()
        exam = session.query(Exam).get(exam_id)
        if exam:
            session.delete(exam)
            session.commit()
        session.close()

    def add_grade(self, student_id, exam_id, grade_value):
        session = self.Session()
        grade = Grade(student_id=student_id, exam_id=exam_id, grade_value=grade_value)
        session.add(grade)
        session.commit()
        session.close()

    def get_all_grades(self):
        session = self.Session()
        grades = session.query(Grade).all()
        session.close()
        return grades

    def update_grade(self, student_id, exam_id, column, new_value):
        session = self.Session()
        grade = session.query(Grade).filter_by(student_id=student_id, exam_id=exam_id).first()
        if grade:
            setattr(grade, column, new_value)
            session.commit()
        session.close()

    def delete_grade(self, student_id, exam_id):
        session = self.Session()
        grade = session.query(Grade).filter_by(student_id=student_id, exam_id=exam_id).first()
        if grade:
            session.delete(grade)
            session.commit()
        session.close()
