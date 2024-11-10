import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="1234",
            dbname="postgres"
        )
        
    # Student operations
    def add_student(self, student_id, first_name, last_name, com_method):
        c = self.conn.cursor()
        c.execute(
            'INSERT INTO "Student" (student_id, first_name, last_name, com_method) VALUES (%s, %s, %s, %s)',
            (student_id, first_name, last_name, com_method)
        )
        self.conn.commit()

    def get_all_students(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Student"')
        return c.fetchall()

    def update_student(self, student_id, column, new_value):
        c = self.conn.cursor()
        c.execute(f'UPDATE "Student" SET {column} = %s WHERE student_id = %s', (new_value, student_id))
        self.conn.commit()

    def delete_student(self, student_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Student" WHERE student_id = %s', (student_id,))
        self.conn.commit()

    # Teacher operations
    def add_teacher(self, teacher_id, first_name, last_name, com_method):
        c = self.conn.cursor()
        c.execute(
            'INSERT INTO "Teacher" (teacher_id, first_name, last_name, com_method) VALUES (%s, %s, %s, %s)',
            (teacher_id, first_name, last_name, com_method)
        )
        self.conn.commit()

    def get_all_teachers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Teacher"')
        return c.fetchall()

    def update_teacher(self, teacher_id, column, new_value):
        c = self.conn.cursor()
        c.execute(f'UPDATE "Teacher" SET {column} = %s WHERE teacher_id = %s', (new_value, teacher_id))
        self.conn.commit()

    def delete_teacher(self, teacher_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Teacher" WHERE teacher_id = %s', (teacher_id,))
        self.conn.commit()

    # Exam operations
    def add_exam(self, exam_id, date, teacher_id):
        c = self.conn.cursor()
        c.execute(
            'INSERT INTO "Exam" (exam_id, date, teacher_id) VALUES (%s, %s, %s)',
            (exam_id, date, teacher_id)
        )
        self.conn.commit()

    def get_all_exams(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Exam"')
        return c.fetchall()

    def update_exam(self, exam_id, column, new_value):
        c = self.conn.cursor()
        c.execute(f'UPDATE "Exam" SET {column} = %s WHERE exam_id = %s', (new_value, exam_id))
        self.conn.commit()

    def delete_exam(self, exam_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Exam" WHERE exam_id = %s', (exam_id,))
        self.conn.commit()

    # Grade operations
    def add_grade(self, student_id, exam_id, grade_value):
        c = self.conn.cursor()
        c.execute(
            'INSERT INTO "Grade" (student_id, exam_id, grade_value) VALUES (%s, %s, %s)',
            (student_id, exam_id, grade_value)
        )
        self.conn.commit()

    def get_all_grades(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM "Grade"')
        return c.fetchall()

    def update_grade(self, student_id, exam_id, column, new_value):
        c = self.conn.cursor()
        c.execute(f'UPDATE "Grade" SET {column} = %s WHERE student_id = %s AND exam_id = %s', (new_value, student_id, exam_id))
        self.conn.commit()

    def delete_grade(self, student_id, exam_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM "Grade" WHERE student_id = %s AND exam_id = %s', (student_id, exam_id))
        self.conn.commit()