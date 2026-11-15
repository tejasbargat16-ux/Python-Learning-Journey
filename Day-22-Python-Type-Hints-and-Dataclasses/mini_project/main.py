import json
from dataclasses import dataclass, field, asdict

FILENAME = "students.json"


@dataclass
class Student:
    roll: int
    name: str
    marks: float
    subjects: list[str] = field(default_factory=list)


def load_students(filename: str = FILENAME) -> list[Student]:
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return [Student(**d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: students.json is corrupted. Starting fresh.")
        return []


def save_students(students: list[Student], filename: str = FILENAME) -> None:
    with open(filename, "w") as f:
        json.dump([asdict(s) for s in students], f, indent=4)


def find_by_roll(students: list[Student], roll: int) -> Student | None:
    for s in students:
        if s.roll == roll:
            return s
    return None


def top_student(students: list[Student]) -> Student | None:
    if not students:
        return None
    return max(students, key=lambda s: s.marks)


def add_student(students: list[Student]) -> None:
    try:
        roll = int(input("Roll number: "))
        if find_by_roll(students, roll):
            print("This roll number already exists.")
            return

        name = input("Name: ").strip()
        marks = float(input("Marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        raw = input("Subjects (comma separated): ")
        subjects = [x.strip() for x in raw.split(",") if x.strip()]
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")
        return

    students.append(Student(roll, name, marks, subjects))
    save_students(students)
    print(f"{name} added successfully.")


def view_all(students: list[Student]) -> None:
    if not students:
        print("No records found.")
        return
    print(f"\n{'Roll':<6}{'Name':<15}{'Marks':<8}Subjects")
    print("-" * 50)
    for s in students:
        print(f"{s.roll:<6}{s.name:<15}{s.marks:<8}{', '.join(s.subjects)}")


def find_student(students: list[Student]) -> None:
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Roll must be a number.")
        return
    student = find_by_roll(students, roll)
    print(student if student else "Student not found.")


def show_topper(students: list[Student]) -> None:
    topper = top_student(students)
    if topper:
        print(f"Topper: {topper.name} with {topper.marks} marks")
    else:
        print("No records found.")


def main() -> None:
    students = load_students()

    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add student")
        print("2. View all")
        print("3. Find by roll")
        print("4. Show topper")
        print("5. Exit")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            show_topper(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
