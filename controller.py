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
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add Student")
        self.view.show_message("2. View Students")
        self.view.show_message("3. Update Student")
        self.view.show_message("4. Delete Student")
        self.view.show_message("5. Quit")
        return input("Enter your choice: ")

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
