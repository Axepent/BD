import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="1234",
            dbname="postgres"
        )

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

