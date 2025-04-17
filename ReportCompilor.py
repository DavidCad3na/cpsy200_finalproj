class ReportCompilor:
    def __init__(self, db):
        self.db = db

    def reportByDate(self):
        # Generates a report of rentals by date
        query = """
        SELECT rentalId, customer, equipment, rentalStartDate, returnDate
        FROM rentals
        ORDER BY rentalStartDate DESC
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return

        print("\n=== Rentals Report by Date ===")
        for rental in results:
            print(f"Rental ID: {rental[0]}, Customer: {rental[1]}, Equipment: {rental[2]}, "
                  f"Rental Date: {rental[3]}, Return Date: {rental[4]}")

    def reportByCustomer(self):
        # Generates a report of rentals by customer
        query = """
        SELECT rentalId, customer, equipment, rentalStartDate, returnDate
        FROM rentals
        ORDER BY customer
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return

        print("\n=== Rentals Report by Customer ===")
        for rental in results:
            print(f"Rental ID: {rental[0]}, Customer: {rental[1]}, Equipment: {rental[2]}, "
                  f"Rental Date: {rental[3]}, Return Date: {rental[4]}")

    def reportEquipmentByCategory(self):
        # Generates a report of equipment grouped by category
        query = """
        SELECT re.equipmentId, re.name, c.category_name
        FROM rental_equipment re
        LEFT JOIN categories c ON re.categoryId = c.categoryId
        ORDER BY c.category_name
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No equipment found.")
            return

        print("\n=== Equipment Report by Category ===")
        for equipment in results:
            equipmentId, name, category_name = equipment
            print(f"Equipment ID: {equipmentId}, Name: {name}, Category: {category_name if category_name else 'Uncategorized'}")
