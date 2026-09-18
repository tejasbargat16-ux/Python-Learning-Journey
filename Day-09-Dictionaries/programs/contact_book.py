contacts = {}

print("=" * 45)
print("           CONTACT BOOK")
print("=" * 45)

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    # Add contact
    if choice == "1":

        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone

        print("Contact saved successfully ")

    # View contacts
    elif choice == "2":

        if len(contacts) == 0:
            print("No contacts found.")

        else:
            print("\n----- CONTACTS -----")

            for name, phone in contacts.items():
                print(name, ":", phone)

    # Search contact
    elif choice == "3":

        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    # Delete contact
    elif choice == "4":

        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")

        else:
            print("Contact not found.")

    # Exit
    elif choice == "5":

        print("\nThanks for using Contact Book! ")
        break

    else:
        print("Invalid option.")
