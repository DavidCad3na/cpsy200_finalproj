# Needed to make some changes for functionality with UI. - Brett
# Created By David Cadena

class CustomerManager:
    def __init__(self, db):
        self.db = db

    def addCustomer(self, customerId, firstname, lastname, contactPhone, email, notes):
        query = """
        INSERT INTO customers (customerId, firstname, lastname, contactPhone, email, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (customerId, firstname, lastname, contactPhone, email, notes))
        print(f"Customer {firstname} {lastname} added to database.")

    def removeCustomer(self, customerID):
        query = "DELETE FROM customers WHERE customerId = %s"
        self.db.execute_query(query, (customerID,))
        print(f"Customer with ID {customerID} removed from database.")

    def viewCustomers(self):
        query = "SELECT * FROM customers"
        results = self.db.fetch_query(query)
        if not results:
            print("No customers found.")
        else:
            print("\n=== Customer List ===")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}, Email: {row[4]}, Notes: {row[5]}")

    def editCustomerDetails(self, customerID):
        query = "SELECT * FROM customers WHERE customerId = %s"
        result = self.db.fetch_query(query, (customerID,))
        if not result:
            print(f"No customer found with ID {customerID}.")
            return

        customer = result[0]
        print(f"Editing details for Customer ID {customerID}:")
        firstname = input("Enter new first name: ") or customer[1]
        lastname = input("Enter new last name: ") or customer[2]
        contactPhone = input("Enter new contact phone: ") or customer[3]
        email = input("Enter new email: ") or customer[4]

        update_query = """
        UPDATE customers 
        SET firstname = %s, lastname = %s, contactPhone = %s, email = %s 
        WHERE customerId = %s
        """
        self.db.execute_query(update_query, (firstname, lastname, contactPhone, email, customerID))
        print(f"Customer ID {customerID} updated successfully.")
