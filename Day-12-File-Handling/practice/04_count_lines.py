try:
    with open("notes.txt", "r") as file:
        lines = file.readlines()

    print("Total lines:", len(lines))

except FileNotFoundError:
    print("notes.txt not found.")