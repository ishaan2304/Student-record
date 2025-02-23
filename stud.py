class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student.student_id] = student
            print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students.values():
                print(student)

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id not in self.students:
            print("Student ID not found.")
        else:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print("Student updated successfully.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            student = Student(student_id, name, age, grade)
            sms.add_student(student)
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            grade = input("Enter new grade (leave blank to keep current): ")
            sms.update_student(student_id, name or None, int(age) if age else None, grade or None)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            sms.delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
