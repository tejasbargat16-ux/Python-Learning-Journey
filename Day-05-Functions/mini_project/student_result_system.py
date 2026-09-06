def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    return sum(marks) / len(marks)


def calculate_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 75:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 40:
        return "D"

    else:
        return "F"


def check_result(percentage):

    if percentage >= 40:
        return "PASS"

    return "FAIL"


print("=" * 45)
print("       🎓 STUDENT RESULT SYSTEM")
print("=" * 45)

name = input("Enter student name: ")

marks1 = float(input("Enter Subject 1 marks: "))
marks2 = float(input("Enter Subject 2 marks: "))
marks3 = float(input("Enter Subject 3 marks: "))

marks = [marks1, marks2, marks3]

total = calculate_total(marks)
percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)
result = check_result(percentage)

print("\n" + "=" * 45)
print("             RESULT")
print("=" * 45)

print("Student:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)

print("=" * 45)
print("       Keep Learning & Building ✓")
print("=" * 45)
