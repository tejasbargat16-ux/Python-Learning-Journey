marks = {
    "Math": 85,
    "Physics": 78,
    "Programming": 92,
    "English": 80
}

highest_subject = ""
highest_marks = 0

for subject, mark in marks.items():

    if mark > highest_marks:
        highest_marks = mark
        highest_subject = subject

print("Highest Marks:", highest_marks)
print("Subject:", highest_subject)
