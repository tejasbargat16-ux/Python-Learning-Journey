age = int(input("Enter your age: "))

if age >= 18:

    has_id = input("Do you have an ID? (yes/no): ").lower()

    if has_id == "yes":
        print("Access granted.")
    else:
        print("ID required.")

else:
    print("You must be 18 or older.")
