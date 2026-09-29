try:
    with open("notes.txt", "r") as file:
        content = file.read()

    keyword = input("Enter keyword to search: ")

    if keyword.lower() in content.lower():
        print("Keyword found! ")
    else:
        print("Keyword not found. ")

except FileNotFoundError:
    print("notes.txt not found.")