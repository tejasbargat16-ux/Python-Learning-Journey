while True:
    try:
        number = int(input("Enter a positive number: "))

        if number <= 0:
            print("Number must be positive.")
            continue

        print("Valid number:", number)
        break

    except ValueError:
        print("Please enter numbers only.")
