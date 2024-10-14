class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Address: {details['address']} , Email: {details['email']}")

    def search_contact(self, search_term):
        results = {name: details for name, details in self.contacts.items() if search_term in name or search_term in details['phone']}
        if not results:
            print("No contacts found.")
        else:
            for name, details in results.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact {name} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")


def main():
    book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            book.update_contact(name, phone, email, address)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()