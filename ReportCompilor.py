# Connor Yasinski (Fixed to work with database)

class ReportCompilor:
    def __init__(self, db):
        self.db = db
        self.report_types = {
            "rental_history": self.generateRentalHistoryReport,
            "inventory_status": self.generateInventoryStatusReport,
            "customer_info": self.generateCustomerInfoReport,
            "category_info": self.generateCategoryReport
        }

    def generateRentalHistoryReport(self):
        print("\n=== Rental History Report ===")
        query = "SELECT rentalId, customer, equipment, rentalStartDate, returnDate, dailyRentalCost, finalRentalCost FROM rentals"
        rentals = self.db.fetch_query(query)

        if not rentals:
            print("No rental history found.")
            return

        for rental in rentals:
            rentalId, customer, equipment, rentalStartDate, returnDate, dailyRentalCost, finalRentalCost = rental
            print(f"Rental ID: {rentalId}, Customer: {customer}, Equipment: {equipment}, "
                  f"Start Date: {rentalStartDate.strftime('%Y-%m-%d') if rentalStartDate else 'N/A'}, "
                  f"Return Date: {returnDate.strftime('%Y-%m-%d') if returnDate else 'N/A'}, "
                  f"Daily Cost: ${dailyRentalCost:.2f}, Final Cost: ${finalRentalCost if finalRentalCost is not None else 'N/A'}")

    def generateInventoryStatusReport(self):
        print("\n=== Inventory Status Report ===")
        query = "SELECT equipmentId, name, available FROM rental_equipment"
        equipment_list = self.db.fetch_query(query)

        if not equipment_list:
            print("No equipment found.")
            return

        for equipment in equipment_list:
            equipmentId, name, available = equipment
            status = "Available" if available else "Rented"
            print(f"Equipment ID: {equipmentId}, Name: {name}, Status: {status}")

    def generateCustomerInfoReport(self):
        print("\n=== Customer Information Report ===")
        query = "SELECT customerId, firstname, lastname, contactPhone, email FROM customers"
        customers = self.db.fetch_query(query)

        if not customers:
            print("No customers found.")
            return

        for customer in customers:
            customerId, firstname, lastname, contactPhone, email = customer
            print(f"Customer ID: {customerId}, Name: {firstname} {lastname}, Phone: {contactPhone}, Email: {email}")

    def generateCategoryReport(self):
        print("\n=== Category Report ===")
        query = "SELECT id, name FROM categories"
        categories = self.db.fetch_query(query)

        if not categories:
            print("No categories found.")
            return

        for category in categories:
            print(f"Category ID: {category[0]}, Name: {category[1]}")
