while True:
    try:
        number = int(input("Enter a number: "))

        print("Valid number:", number)
        break

    except ValueError:
        print("Invalid input! Please enter an integer.")
