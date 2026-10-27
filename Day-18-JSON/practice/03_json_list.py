import json

students = [
    {"name": "Tejas", "marks": 85},
    {"name": "Aman", "marks": 90},
    {"name": "Rahul", "marks": 78}
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("Students saved successfully!")

with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)

print("\nStudent Records:")

for student in loaded_students:
    print(f"{student['name']} - {student['marks']} marks")
