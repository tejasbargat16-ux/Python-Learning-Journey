import random
import string

try:
    length = int(input("Enter password length: "))

    if length < 1:
        print("Length must be at least 1.")

    else:
        characters = string.ascii_letters + string.digits

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated password:", password)

except ValueError:
    print("Please enter a valid integer.")
