age = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ").lower()

is_student = student == "yes"

eligible = age >= 18 and is_student

print("\n----- ELIGIBILITY -----")
print("Age:", age)
print("Student:", is_student)
print("Eligible:", eligible)
