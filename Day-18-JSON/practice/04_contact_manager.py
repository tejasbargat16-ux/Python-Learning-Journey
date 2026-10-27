import json
from pathlib import Path

FILE_PATH = Path(__file__).with_name("contacts.json")


def load_contacts():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            contacts = json.load(file)

        if not isinstance(contacts, list):
            print("Invalid contacts data.")
            return []

        return contacts

    except json.JSONDecodeError:
        print("Contacts file contains invalid JSON.")
        return []


def save_contacts(contacts):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone cannot be empty.")
        return

    contacts.append({
        "name": name,
        "phone": phone
    })

    save_contacts(contacts)
    print("Contact saved successfully!")


def show_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nSaved Contacts:")

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
