class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self._salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self._salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


employee1 = Employee("Aman", 25000)
manager1 = Manager("Tejas", 50000, "Technology")

print("--- Employee Details ---")
employee1.display()

print("\n--- Manager Details ---")
manager1.display()
