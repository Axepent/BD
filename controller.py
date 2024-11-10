from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.add_teacher()
            elif choice == '6':
                self.view_teachers()
            elif choice == '7':
                self.update_teacher()
            elif choice == '8':
                self.delete_teacher()
            elif choice == '9':
                self.add_exam()
            elif choice == '10':
                self.view_exams()
            elif choice == '11':
                self.update_exam()
            elif choice == '12':
                self.delete_exam()
            elif choice == '13':
                self.add_grade()
            elif choice == '14':
                self.view_grades()
            elif choice == '15':
                self.update_grade()
            elif choice == '16':
                self.delete_grade()
            elif choice == '17':
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add Student")
        self.view.show_message("2. View Students")
        self.view.show_message("3. Update Student")
        self.view.show_message("4. Delete Student")
        self.view.show_message("5. Add Teacher")
        self.view.show_message("6. View Teachers")
        self.view.show_message("7. Update Teacher")
        self.view.show_message("8. Delete Teacher")
        self.view.show_message("9. Add Exam")
        self.view.show_message("10. View Exams")
        self.view.show_message("11. Update Exam")
        self.view.show_message("12. Delete Exam")
        self.view.show_message("13. Add Grade")
        self.view.show_message("14. View Grades")
        self.view.show_message("15. Update Grade")
        self.view.show_message("16. Delete Grade")
        self.view.show_message("17. Quit")
        return input("Enter your choice: ")

    # Student operations
    def add_student(self):
        student_id, first_name, last_name, com_method = self.view.get_student_input()
        self.model.add_student(student_id, first_name, last_name, com_method)
        self.view.show_message("Student added successfully!")

    def view_students(self):
        students = self.model.get_all_students()
        self.view.show_students(students)

    def update_student(self):
        student_id = self.view.get_student_id()
        column = input("Enter column to update (first_name, last_name, com_method): ")
        new_value = input("Enter new value: ")
        self.model.update_student(student_id, column, new_value)
        self.view.show_message("Student updated successfully!")

    def delete_student(self):
        student_id = self.view.get_student_id()
        self.model.delete_student(student_id)
        self.view.show_message("Student deleted successfully!")

    # Teacher operations
    def add_teacher(self):
        teacher_id, first_name, last_name, com_method = self.view.get_teacher_input()
        self.model.add_teacher(teacher_id, first_name, last_name, com_method)
        self.view.show_message("Teacher added successfully!")

    def view_teachers(self):
        teachers = self.model.get_all_teachers()
        self.view.show_teachers(teachers)

    def update_teacher(self):
        teacher_id = self.view.get_teacher_id()
        column = input("Enter column to update (first_name, last_name, com_method): ")
        new_value = input("Enter new value: ")
        self.model.update_teacher(teacher_id, column, new_value)
        self.view.show_message("Teacher updated successfully!")

    def delete_teacher(self):
        teacher_id = self.view.get_teacher_id()
        self.model.delete_teacher(teacher_id)
        self.view.show_message("Teacher deleted successfully!")

    # Exam operations
    def add_exam(self):
        exam_id, date, teacher_id = self.view.get_exam_input()
        self.model.add_exam(exam_id, date, teacher_id)
        self.view.show_message("Exam added successfully!")

    def view_exams(self):
        exams = self.model.get_all_exams()
        self.view.show_exams(exams)

    def update_exam(self):
        exam_id = self.view.get_exam_id()
        column = input("Enter column to update (date, teacher_id): ")
        new_value = input("Enter new value: ")
        self.model.update_exam(exam_id, column, new_value)
        self.view.show_message("Exam updated successfully!")

    def delete_exam(self):
        exam_id = self.view.get_exam_id()
        self.model.delete_exam(exam_id)
        self.view.show_message("Exam deleted successfully!")


    # Grade operations
    def add_grade(self):
        student_id, exam_id, grade_value = self.view.get_grade_input()
        self.model.add_grade(student_id, exam_id, grade_value)
        self.view.show_message("Grade added successfully!")

    def view_grades(self):
        grades = self.model.get_all_grades()
        self.view.show_grades(grades)

    def update_grade(self):
        student_id = self.view.get_student_id()
        exam_id = self.view.get_exam_id()
        column = input("Enter column to update (grade_value): ")
        new_value = input("Enter new value: ")
        self.model.update_grade(student_id, exam_id, column, new_value)
        self.view.show_message("Grade updated successfully!")

    def delete_grade(self):
        student_id, exam_id = self.view.get_grade_id()
        self.model.delete_grade(student_id, exam_id)
        self.view.show_message("Grade deleted successfully!")
