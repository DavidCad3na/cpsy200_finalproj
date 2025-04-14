customers = []
customerID = 0
firstname = ""
lastname = ""
contactPhone = ""
email = ""
notes = ""

def addCustomer(customerId, firstname, lastname, contactPhone, Email, notes):
    global customers
    new_customer = {
        'customerId': customerId,
        'firstname': firstname,
        'lastname': lastname,
        'contactPhone': contactPhone,
        'Email': Email,
        'notes': notes
    }

    customers.append(new_customer)
    return new_customer

def removeCustomer(customerID):
    global rental
    rental = [customer for customer in customers if customer['customerID'] != customerID]
    print(f"Customer with ID {customerID} has been removed.")

def viewCustomers():
    global customers
    return customers

def editCustomerDetails(customerID):
    global customers
    for customer in customers:
        if customer['customerID'] == customerID:

            newfirstname = print("Enter new first name: ")
            customer['firstname'] = newfirstname

            newlastname = print("Enter new last name: ")
            customer['lastname'] = newlastname

            newContactPhone = input("Enter new contact phone: ")
            customer['contactPhone'] = newContactPhone

            newEmail = input("Enter new email: ")
            customer['email'] = newEmail
            break