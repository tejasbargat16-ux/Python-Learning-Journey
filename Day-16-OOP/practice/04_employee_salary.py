class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            print("Salary cannot be negative!")

    def display(self):
        print("Employee:", self.name)
        print("Salary: ₹", self.salary)


employee1 = Employee("Aman", 25000)

employee1.display()

employee1.salary = 30000

print("\nUpdated salary:")
employee1.display()

employee1.salary = -1000

print("\nAfter invalid update:")
employee1.display()
