from datetime import timedelta

class ReportCompilor:
    def __init__(self, db):
        self.db = db

    def reportByDate(self):
        # Generates a report of rentals by start date
        query = """
        SELECT rentalId, customerId, equipmentId, startDate, daysRented
        FROM rentals
        ORDER BY startDate DESC
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return

        print("\n=== Rentals Report by Date ===")
        for rental in results:
            rentalId, customerId, equipmentId, startDate, daysRented = rental
            return_date = startDate + timedelta(days=daysRented) if startDate and daysRented else "N/A"
            print(f"Rental ID: {rentalId}, Customer ID: {customerId}, Equipment ID: {equipmentId}, "
                  f"Start Date: {startDate.strftime('%Y-%m-%d') if startDate else 'N/A'}, "
                  f"Days Rented: {daysRented if daysRented is not None else 'N/A'}")

    def reportByCustomer(self):
        query = """
        SELECT rentalId, customerId, equipmentId, startDate, daysRented
        FROM rentals
        ORDER BY customerId
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return

        print("\n=== Rentals Report by Customer ===")
        for rental in results:
            rentalId, customerId, equipmentId, startDate, daysRented = rental
            print(f"Rental ID: {rentalId}, Customer ID: {customerId}, Equipment ID: {equipmentId}, "
                f"Start Date: {startDate.strftime('%Y-%m-%d') if startDate else 'N/A'}, "
                f"Days Rented: {daysRented if daysRented is not None else 'N/A'}")


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
