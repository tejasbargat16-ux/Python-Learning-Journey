try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age.")

    elif age > 120:
        print("Invalid age.")

    else:
        print("Valid age:", age)

except ValueError:
    print("Please enter a valid number.")
