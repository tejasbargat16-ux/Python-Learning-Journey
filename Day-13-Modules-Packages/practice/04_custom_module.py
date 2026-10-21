from calculator import add, subtract, multiply, divide

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    print("Addition:", add(first, second))
    print("Subtraction:", subtract(first, second))
    print("Multiplication:", multiply(first, second))
    print("Division:", divide(first, second))

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError as error:
    print("Error:", error)
