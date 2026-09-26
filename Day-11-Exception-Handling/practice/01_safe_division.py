try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
