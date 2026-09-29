try:
    with open("notes.txt", "r") as source:
        content = source.read()

    with open("backup_notes.txt", "w") as backup:
        backup.write(content)

    print("Backup created successfully. ")

except FileNotFoundError:
    print("notes.txt not found.")