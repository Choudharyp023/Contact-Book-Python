# A simple Contact Book application built using Python dictionaries and functions.

def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter the contact name: ")

    if name in contact_book:
        print("Contact already exists!")
        return

    phone = input("Enter the phone number: ")
    email = input("Enter the email id: ")
    address = input("Enter the address: ")

    contact_book[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }

    print("Contact added successfully!")


def view_contact(contact_book):
    name = input("Enter the contact name: ")

    if name in contact_book:
        contact = contact_book[name]

        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")


def edit_contact(contact_book):
    name = input("Enter the contact name: ")

    if name in contact_book:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email id: ")
        address = input("Enter the new address: ")

        if phone == "":
            phone = contact_book[name]['phone']

        if email == "":
            email = contact_book[name]['email']

        if address == "":
            address = contact_book[name]['address']

        contact_book[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }

        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact(contact_book):
    name = input("Enter the contact name: ")

    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, contact in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()  # Blank line between contacts for readability


# Contact book dictionary
contact_book = {}

# While loop for Main Menu
while True:
    display_menu()
    choice = input("Please choose a menu option: ")

    if choice == '1':
        add_contact(contact_book)
    elif choice == '2':
        view_contact(contact_book)
    elif choice == '3':
        edit_contact(contact_book)
    elif choice == '4':
        delete_contact(contact_book)
    elif choice == '5':
        list_all_contacts(contact_book)
    elif choice == '6':
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please try again.")
