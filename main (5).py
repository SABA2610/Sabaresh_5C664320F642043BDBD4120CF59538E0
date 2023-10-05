def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    student_list.sort(key=lambda student: student.cgpa, reverse=True)

# Define a Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("Alice", "001", 3.9),
    Student("Bob", "002", 3.7),
    Student("Charlie", "003", 3.5),
    Student("David", "004", 4.0),
]

# Test the sort_students function
sort_students(students)

# Print the sorted list
for student in students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")