class View:
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
