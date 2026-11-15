class Student:
    def __init__(self, name, roll, marks=0.0):
        self.name = name
        self.roll = roll
        self.marks = marks

    def __repr__(self):
        return f"Student(name={self.name!r}, roll={self.roll}, marks={self.marks})"

    def __eq__(self, other):
        return (self.name, self.roll, self.marks) == (other.name, other.roll, other.marks)


print(Student("Tejas", 1, 85.5))
