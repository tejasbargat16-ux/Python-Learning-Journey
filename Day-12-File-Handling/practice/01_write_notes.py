note = input("Enter your note: ")

with open("notes.txt", "w") as file:
    file.write(note + "\n")

print("Note saved successfully. ")