class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


student1 = Student("Tejas", 85)
student2 = Student("Aman", 32)

print("Student:", student1.name)
student1.check_result()

print("\nStudent:", student2.name)
student2.check_result()
