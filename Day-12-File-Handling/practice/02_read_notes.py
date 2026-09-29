try:
    with open("notes.txt", "r") as file:
        content = file.read()

    print("\n===== YOUR NOTES =====")
    print(content)

except FileNotFoundError:
    print("notes.txt not found.")