try:
    marks = float(input("Enter your marks: "))

    if marks < 0:
        print("Invalid marks.")

    elif marks > 100:
        print("Invalid marks.")

    else:
        print("Valid marks:", marks)

except ValueError:
    print("Please enter a valid number.")
