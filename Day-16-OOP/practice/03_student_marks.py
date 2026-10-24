class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Marks must be between 0 and 100!")

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student1 = Student("Tejas", 85)

student1.display()

student1.marks = 95
print("\nAfter updating:")
student1.display()

student1.marks = 150
print("\nAfter invalid update:")
student1.display()
