import random
import datetime

from calculator import add, subtract, multiply, divide
from converter import celsius_to_fahrenheit, kilometers_to_miles
from greetings import welcome


name = input("Enter your name: ")

print(welcome(name))

while True:

    print("\n==============================")
    print("     SMART UTILITY TOOLKIT")
    print("==============================")

    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. Distance Converter")
    print("4. Random Number")
    print("5. Current Date & Time")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        first = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", add(first, second))

        elif operator == "-":
            print("Result:", subtract(first, second))

        elif operator == "*":
            print("Result:", multiply(first, second))

        elif operator == "/":
            result = divide(first, second)

            if result is None:
                print("Cannot divide by zero.")

            else:
                print("Result:", result)

        else:
            print("Invalid operator.")

    elif choice == "2":

        celsius = float(input("Enter Celsius: "))

        result = celsius_to_fahrenheit(celsius)

        print("Fahrenheit:", result)

    elif choice == "3":

        kilometers = float(input("Enter kilometers: "))

        result = kilometers_to_miles(kilometers)

        print("Miles:", result)

    elif choice == "4":

        number = random.randint(1, 100)

        print("Random number:", number)

    elif choice == "5":

        current = datetime.datetime.now()

        print("Current date:", current.date())
        print("Current time:", current.time())

    elif choice == "6":

        print("Toolkit closed. 👋")
        break

    else:

        print("Invalid choice.")
