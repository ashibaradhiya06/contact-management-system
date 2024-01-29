import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts =json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone):
    if name in contacts:
        print(f"Contact with name '{name}' already exists.")
    else:
        contacts[name] = {'phone': phone}
        save_contacts(contacts)
        print(f"Contact '{name}' added successfully.")

def search_contact(contacts, name):
    if name in contacts:
        contact_info = contacts[name]
        print(f"Contact Information for '{name}':")
        print(f"Phone: {contact_info['phone']}")
    else:
        print(f"Contact with name '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()
