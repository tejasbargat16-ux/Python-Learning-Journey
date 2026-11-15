from dataclasses import dataclass, field


@dataclass
class Employee:
    name: str
    monthly_salary: float
    annual_salary: float = field(init=False)

    def __post_init__(self):
        if self.monthly_salary <= 0:
            raise ValueError("Salary must be greater than 0")
        self.annual_salary = self.monthly_salary * 12


print(Employee("Tejas", 25000))

try:
    Employee("Rahul", -500)
except ValueError as e:
    print("Error:", e)
