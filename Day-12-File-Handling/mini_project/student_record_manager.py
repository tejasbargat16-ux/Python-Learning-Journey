FILE_NAME = "students.txt"


def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("Student added successfully. ")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        if not students:
            print("No student records found.")
            return

        print("\n===== STUDENT RECORDS =====")

        for student in students:
            name, age, course = student.strip().split(",")

            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Course: {course}")
            print("-" * 30)

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search_name = input("Enter student name: ").lower()

    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

        found = False

        for student in students:
            name, age, course = student.strip().split(",")

            if name.lower() == search_name:
                print("\nStudent Found!")
                print("Name:", name)
                print("Age:", age)
                print("Course:", course)

                found = True
                break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


while True:

    print("\n==============================")
    print("     STUDENT RECORD MANAGER")
    print("==============================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program closed. ")
        break

    else:
        print("Invalid choice.")