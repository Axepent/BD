class View:
    # Student methods
    def show_students(self, students):
        print("Students:")
        for student in students:
            print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}, Communication Method: {student[3]}")

    def get_student_input(self):
        student_id = int(input("Enter student ID: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        com_method = input("Enter communication method (e.g., email, phone): ")
        return student_id, first_name, last_name, com_method

    def get_student_id(self):
        return int(input("Enter student ID: "))

    def show_message(self, message):
        print(message)


    # Teacher methods
    def show_teachers(self, teachers):
        print("Teachers:")
        for teacher in teachers:
            print(f"ID: {teacher[0]}, First Name: {teacher[1]}, Last Name: {teacher[2]}, Communication Method: {teacher[3]}")

    def get_teacher_input(self):
        teacher_id = int(input("Enter teacher ID: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        com_method = input("Enter communication method (e.g., email, phone): ")
        return teacher_id, first_name, last_name, com_method
    
    def get_teacher_id(self):
        return int(input("Enter teacher ID: "))

    def show_message(self, message):
        print(message)

    # Exam methods
    def show_exams(self, exams):
        print("Exams:")
        for exam in exams:
            print(f"ID: {exam[0]}, Date: {exam[1]}, Teacher ID: {exam[2]}")

    def get_exam_input(self):
        exam_id = int(input("Enter exam ID: "))
        date = input("Enter exam date (YYYY-MM-DD): ")
        teacher_id = int(input("Enter teacher ID for the exam: "))
        return exam_id, date, teacher_id
    
    def get_exam_id(self):
        return int(input("Enter exam ID: "))

    def show_message(self, message):
        print(message)

    # Grade methods
    def show_grades(self, grades):
        print("Grades:")
        for grade in grades:
            print(f"Student ID: {grade[0]}, Exam ID: {grade[1]}, Grade: {grade[2]}")

    def get_grade_input(self):
        student_id = int(input("Enter student ID: "))
        exam_id = int(input("Enter exam ID: "))
        grade_value = int(input("Enter grade value: "))
        return student_id, exam_id, grade_value

    def get_grade_id(self):
        student_id = int(input("Enter student ID: "))
        exam_id = int(input("Enter exam ID: "))
        return student_id, exam_id

    def show_message(self, message):
        print(message)