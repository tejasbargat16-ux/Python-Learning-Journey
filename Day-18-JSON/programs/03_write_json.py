import json

student = {
    "name": "Tejas",
    "roll_no": 18,
    "marks": 85
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Student data saved successfully!")
