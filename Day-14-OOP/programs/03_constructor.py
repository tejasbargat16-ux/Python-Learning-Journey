class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


student1 = Student("Tejas", 14, 85)
student2 = Student("Aman", 15, 90)

print(student1.name, student1.roll_no, student1.marks)
print(student2.name, student2.roll_no, student2.marks)
