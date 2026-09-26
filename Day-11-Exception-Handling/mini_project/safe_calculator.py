print("================================")
print("       SAFE CALCULATOR")
print("================================")

while True:

    try:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("\nCalculator closed.")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice.")
            continue

        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        if choice == "1":
            result = first + second
            operation = "Addition"

        elif choice == "2":
            result = first - second
            operation = "Subtraction"

        elif choice == "3":
            result = first * second
            operation = "Multiplication"

        elif choice == "4":
            result = first / second
            operation = "Division"

        elif choice == "5":
            result = first % second
            operation = "Modulus"

        print("\nOperation:", operation)
        print("Result:", result)

    except ValueError:
        print("\nError: Please enter valid numbers.")

    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")

    except Exception as error:
        print("\nUnexpected error:", error)

    print("\n--------------------------------")
