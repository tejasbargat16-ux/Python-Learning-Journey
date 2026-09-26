try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Zero is not allowed.")
