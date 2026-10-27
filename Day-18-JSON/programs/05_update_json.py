import json

filename = "student.json"

try:
    with open(filename, "r", encoding="utf-8") as file:
        student = json.load(file)

    student["marks"] = 95
    student["skills"] = ["Python", "Java", "JSON"]

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(student, file, indent=4)

    print("Student data updated!")
    print(student)

except FileNotFoundError:
    print("Run the write program first.")

except json.JSONDecodeError:
    print("Invalid JSON data.")
