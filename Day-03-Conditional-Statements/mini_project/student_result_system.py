print("=" * 45)
print("======= STUDENT RESULT SYSTEM =======")
print("=" * 45)

name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\n" + "=" * 45)
print("===== RESULT =====")
print("=" * 45)

print("Student:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Grade:", grade)
print("Result:", result)

print("=" * 45)
print("==== Keep Learning ==== ")
print("=" * 45)

