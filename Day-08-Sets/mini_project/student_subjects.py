print("=" * 45)
print("        STUDENT SUBJECT TRACKER")
print("=" * 45)

student1 = set()
student2 = set()

print("\nEnter subjects for Student 1")
for i in range(3):
    subject = input("Enter subject: ")
    student1.add(subject)

print("\nEnter subjects for Student 2")
for i in range(3):
    subject = input("Enter subject: ")
    student2.add(subject)

print("\n" + "=" * 45)
print("             RESULTS")
print("=" * 45)

print("Student 1:", student1)
print("Student 2:", student2)

common = student1 & student2
only_student1 = student1 - student2
only_student2 = student2 - student1
all_subjects = student1 | student2

print("\nCommon subjects:", common)
print("Only Student 1:", only_student1)
print("Only Student 2:", only_student2)
print("All subjects:", all_subjects)

print("=" * 45)
