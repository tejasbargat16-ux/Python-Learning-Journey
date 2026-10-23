class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Tejas", 85)

student1.display()
