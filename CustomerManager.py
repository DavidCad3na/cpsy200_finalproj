# Needed to make some changes for functionality with UI. - Brett
# Created By David Cadena
class CustomerManager:
    def __init__(self):
        # Initialize instance variables
        self.customers = []
        self.customerID = 0

    def addCustomer(self, customerId, firstname, lastname, contactPhone, email, notes):
        new_customer = {
            'customerId': customerId,
            'firstname': firstname,
            'lastname': lastname,
            'contactPhone': contactPhone,
            'email': email,
            'notes': notes
        }
        self.customers.append(new_customer)
        print(f"Customer {firstname} {lastname} added successfully.")
        return new_customer

    def removeCustomer(self, customerID):
        self.customers = [customer for customer in self.customers if customer['customerId'] != customerID]
        print(f"Customer with ID {customerID} has been removed.")

    def viewCustomers(self):
        if not self.customers:
            print("No customers found.")
        else:
            print("\n=== Customer List ===")
            for customer in self.customers:
                print(f"ID: {customer['customerId']}, Name: {customer['firstname']} {customer['lastname']}, "
                      f"Phone: {customer['contactPhone']}, Email: {customer['email']}, Notes: {customer['notes']}")

    def editCustomerDetails(self, customerID):
        for customer in self.customers:
            if customer['customerId'] == customerID:
                print(f"Editing details for Customer ID {customerID}:")
                customer['firstname'] = input("Enter new first name: ") or customer['firstname']
                customer['lastname'] = input("Enter new last name: ") or customer['lastname']
                customer['contactPhone'] = input("Enter new contact phone: ") or customer['contactPhone']
                customer['email'] = input("Enter new email: ") or customer['email']
                print(f"Customer ID {customerID} updated successfully.")
                return
        print(f"No customer found with ID {customerID}.")