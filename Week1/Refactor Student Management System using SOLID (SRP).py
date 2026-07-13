class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        return "Fail"

    def save_student(self):
        print("Saving student to database...")

    def print_report(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


student = Student("John", 85)
student.print_report()
student.save_student()