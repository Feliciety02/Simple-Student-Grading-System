# Simple Student Grading System
# By: [Your Name]
# Description: Record student grades, calculate average, and display letter grade

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # Method to add grades for 3 subjects
    def add_grades(self):
        print(f"\nEnter grades for {self.name}:")
        for i in range(1, 4):
            while True:
                try:
                    grade = float(input(f"Subject {i} grade: "))
                    if 0 <= grade <= 100:
                        self.grades.append(grade)
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

    # Method to calculate average
    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    # Method to get letter grade based on average
    def get_grade_letter(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    # Method to display student info
    def display_info(self):
        avg = self.calculate_average()
        letter = self.get_grade_letter()
        print("\n--- Student Info ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.2f}")
        print(f"Letter Grade: {letter}")
        print("-------------------")

# ------------------- MAIN PROGRAM -------------------

print("=== SIMPLE STUDENT GRADING SYSTEM ===")

# Input student info
name = input("Enter student name: ")
student_id = input("Enter student ID: ")

# Create Student object
student = Student(name, student_id)

# Add grades
student.add_grades()

# Display student info and average
student.display_info()
