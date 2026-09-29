try:
    with open("notes.txt", "r") as file:
        content = file.read()

    word = input("Enter word: ")

    count = content.lower().count(word.lower())

    print(f"'{word}' appears {count} time(s).")

except FileNotFoundError:
    print("notes.txt not found.")