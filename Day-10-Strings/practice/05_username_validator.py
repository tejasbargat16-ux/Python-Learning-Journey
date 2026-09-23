username = input("Enter username: ")
has_letter = False

for char in username:
    if char.isalpha():
        has_letter = True
        break

if len(username) < 5:
    print("Invalid Username")
    print("Username must contain at least 5 characters.")

elif " " in username:
    print("Invalid Username")
    print("Username must not contain spaces.")

elif not has_letter:
    print("Invalid Username")
    print("Username must contain at least one letter.")

else:
    print("Valid Username")
