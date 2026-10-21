import math

try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root of a negative number is not supported here.")

    else:
        square_root = math.sqrt(number)

        print("Square root:", square_root)
        print("Square:", number ** 2)
        print("Cube:", number ** 3)

except ValueError:
    print("Please enter a valid number.")
