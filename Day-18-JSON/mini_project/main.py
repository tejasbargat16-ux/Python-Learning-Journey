import json
from pathlib import Path

FILE_PATH = Path(__file__).with_name("students.json")


def load_students():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid data format.")
            return []

        return data

    except json.JSONDecodeError:
        print("The JSON file is invalid.")
        return []


def save_students(students):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    students.append({
        "name": name,
        "marks": marks
    })

    save_students(students)
    print("Student saved successfully!")


def show_students(students):
    if not students:
        print("No student records found.")
        return

    for index, student in enumerate(students, start=1):
        print(
            f"{index}. {student['name']} "
            f"- {student['marks']} marks"
        )


def main():
    students = load_students()

    while True:
        print("\n--- Student Data Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
