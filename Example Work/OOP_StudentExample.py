from datetime import date

class Student:

    number_of_students = 0
    def __init__(self, name, age):
        Student.number_of_students += 1
        self.id = Student.number_of_students
        self.name = name
        self.age = age

    def introduce_yourself(self):
        print(f"Hello, I am Student with ID {self.id}.\nMy name is {self.name} and I am {self.age} years old!")

    @classmethod
    def get_number_of_students(cls):
        return f"There are {Student.number_of_students} students in total."






# Example usage
if __name__ == "__main__":
    student_1 = Student('Tom', 45)
    student_2 = Student('Jim', 17)
    student_1.introduce_yourself()
    student_2.introduce_yourself()

    print(Student.get_number_of_students())

