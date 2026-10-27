import json

try:
    with open("student.json", "r", encoding="utf-8") as file:
        student = json.load(file)

    print("Name:", student["name"])
    print("Roll No:", student["roll_no"])
    print("Marks:", student["marks"])

except FileNotFoundError:
    print("student.json not found. Run the write program first.")

except json.JSONDecodeError:
    print("The JSON file contains invalid JSON.")
