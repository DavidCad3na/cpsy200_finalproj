#Connor Yasinski
import RentalManager
from db_manager import DatabaseManager
from CustomerManager import CustomerManager
from RentalEquipmentList import RentalEquipmentList
from RentalManager import RentalManager
from CategoryList import CategoryList

#Class Might need additional options
    def __init__(self):
        self.db = DatabaseManager()
        self.category_list = CategoryList(self.db)  # Initialize CategoryList
        self.customer_manager = CustomerManager(self.db)
        self.rental_equipment_list = RentalEquipmentList(self.db)  # Initialize RentalEquipmentList first (Must be in this order)
        self.rental_manager = RentalManager(self.rental_equipment_list)  # Pass it to RentalManager (For these 2)
            "customer_info": self.generateCustomerInfoReport
   #Maybe add a function to search the database

    def reportByDate(self):
        #Generates a report of rentals by date.
        query = """
        SELECT rentalId, customerId, equipmentId, rentalDate, returnDate
        FROM rentals
        ORDER BY rentalDate DESC
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return
        print("\n=== Rentals Report by Date ===")
        for rental in results:
            print(f"Rental ID: {rental[0]}, Customer ID: {rental[1]}, Equipment ID: {rental[2]}, Rental Date: {rental[3]}, Return Date: {rental[4]}")

    def reportByCustomer(self):
        #Generates a report of rentals by customer.
        query = """
        SELECT rentalId, customerId, equipmentId, rentalDate, returnDate
        FROM rentals
        ORDER BY customerId
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return
        print("\n=== Rentals Report by Customer ===")
        for rental in results:
            print(f"Rental ID: {rental[0]}, Customer ID: {rental[1]}, Equipment ID: {rental[2]}, Rental Date: {rental[3]}, Return Date: {rental[4]}")
                  f"Daily Rental Cost: ${equipment['dailyRentalCost']:.2f}, "
    def reportEquipmentByCategory(self):
        #Generates a report of rentals by equipment category.
        query = """
        SELECT rentalId, customerId, equipmentId, rentalDate, returnDate
        FROM rentals
        ORDER BY equipmentId
        """
        results = self.db.fetch_query(query)
        if not results:
            print("No rentals found.")
            return
        print("\n=== Rentals Report by Equipment Category ===")
        for rental in results:
            print(f"Rental ID: {rental[0]}, Customer ID: {rental[1]}, Equipment ID: {rental[2]}, Rental Date: {rental[3]}, Return Date: {rental[4]}")
            
                
    