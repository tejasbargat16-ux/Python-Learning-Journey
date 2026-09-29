note = input("Enter a new note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("New note added successfully. ")