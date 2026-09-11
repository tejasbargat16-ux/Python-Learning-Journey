print("=" * 45)
print("           EMPLOYEE RECORD")
print("=" * 45)

name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
role = input("Enter employee role: ")
salary = float(input("Enter employee salary: "))

employee = (name, age, role, salary)

print("\n" + "=" * 45)
print("           EMPLOYEE DETAILS")
print("=" * 45)

print("Name:", employee[0])
print("Age:", employee[1])
print("Role:", employee[2])
print("Salary:", employee[3])

print("=" * 45)
print("Record created successfully ")
print("=" * 45)
