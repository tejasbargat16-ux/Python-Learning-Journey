try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Age must be a number.")
