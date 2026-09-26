try:
    first = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second = float(input("Enter second number: "))

    if operator == "+":
        result = first + second

    elif operator == "-":
        result = first - second

    elif operator == "*":
        result = first * second

    elif operator == "/":
        result = first / second

    else:
        print("Invalid operator.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
