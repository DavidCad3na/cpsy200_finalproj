# Created by Brett Shalagan

from db_manager import DatabaseManager
from CustomerManager import CustomerManager
from RentalEquipmentList import RentalEquipmentList
from RentalManager import RentalManager
from ReportCompilor import ReportCompilor
from CategoryList import CategoryList

class UserInterface:
    """
        User Interface class for managing the rental equipment system.
    """
    def __init__(self):
        """
            Dependencies
        """
        self.db = DatabaseManager()
        self.category_list = CategoryList(self.db)
        self.customer_manager = CustomerManager(self.db)
        self.rental_equipment_list = RentalEquipmentList(self.db)
        self.rental_manager = RentalManager(self.db, self.rental_equipment_list)
        self.report_compilor = ReportCompilor(self.db)

    def systemManager(self):
        """
            System Manager Menu
        """
        while True:
            print("\n=== System Manager ===")
            print("1. Reset Inventory Data")
            print("2. View System Status")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Reset inventory data
                confirm = input("Are you sure you want to reset all inventory data? (yes/no): ").strip().lower()
                if confirm == "yes":
                    query = "DELETE FROM rental_equipment"
                    self.db.execute_query(query)
                    print("All inventory data has been reset.")
                else:
                    print("Reset operation canceled.")
            elif choice == "2":
                # View system status
                print("\n=== System Status ===")
                print(f"Total Equipment in Inventory: {len(self.db.fetch_query('SELECT * FROM rental_equipment'))}")
                print(f"Total Rentals: {len(self.db.fetch_query('SELECT * FROM rentals'))}")
                print(f"Total Customers: {len(self.db.fetch_query('SELECT * FROM customers'))}")
            elif choice == "3":
                # Return to main menu
                break
            else:
                print("Invalid choice. Please try again.")

    def manageInventory(self):
        """
            Inventory Management Menu
        """
        while True:
            print("\n=== Manage Inventory ===")
            print("1. View Inventory")
            print("2. Add New Equipment")
            print("3. Remove Equipment")
            print("4. Update Equipment Availability")
            print("5. Manage Equipment Categories")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                # View all inventory items
                self.rental_equipment_list.viewRentalEquipment()
            elif choice == "2":
                # Add new equipment
                equipment_id = input("Enter Equipment ID: ")
                name = input("Enter Equipment Name: ")
                available = input("Is the equipment available? (yes/no): ").strip().lower() == "yes"
                category_id = input("Enter Category ID: ")
                self.rental_equipment_list.addRentalEquipment({
                    'equipmentId': equipment_id,
                    'name': name,
                    'available': available,
                    'categoryId': category_id
                })
            elif choice == "3":
                # Remove equipment
                equipment_id = input("Enter Equipment ID to remove: ")
                self.rental_equipment_list.removeRentalEquipment(equipment_id)
            elif choice == "4":
                # Update equipment availability
                equipment_id = input("Enter Equipment ID to update availability: ")
                availability = input("Is the equipment available? (yes/no): ").strip().lower() == "yes"
                if availability:
                    self.rental_equipment_list.markAsReturned(equipment_id)
                else:
                    self.rental_equipment_list.markAsRented(equipment_id)
            elif choice == "5":
                # Manage equipment categories
                self.manageCategories()
            elif choice == "6":
                # Return to main menu
                break
            else:
                print("Invalid choice. Please try again.")

    def manageCategories(self):
        """
            Equipment Category Management Menu
        """
        while True:
            print("\n=== Manage Equipment Categories ===")
            print("1. View Categories")
            print("2. Add Category")
            print("3. Remove Category")
            print("4. Back to Inventory Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                # View all categories
                self.category_list.viewCategory()
            elif choice == "2":
                # Add a new category
                category_id = input("Enter Category ID: ")
                category_name = input("Enter Category Name: ")
                self.category_list.addCategory(category_id, category_name)
            elif choice == "3":
                # Remove a category
                category_id = input("Enter Category ID to remove: ")
                self.category_list.removeCategory(category_id)
            elif choice == "4":
                # Return to inventory menu
                break
            else:
                print("Invalid choice. Please try again.")

    def equipmentRental(self):
        """
            Equipment Rental Menu
        """ 
        while True:
            print("\n=== Equipment Rental ===")
            print("1. Rent Equipment")
            print("2. Return Equipment")
            print("3. View Rented Equipment")
            print("4. Calculate Rental Cost")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Rent equipment
                rental_id = input("Enter Rental ID: ")
                rental_start_date = input("Enter Rental Start Date (YYYY-MM-DD): ")
                customer = input("Enter Customer Name: ")
                equipment = input("Enter Equipment Name: ")
                daily_rental_cost = input("Enter Daily Rental Cost: ")
                self.rental_manager.addRental(rental_id, rental_start_date, customer, equipment, daily_rental_cost)
            elif choice == "2":
                # Return equipment
                rental_id = input("Enter Rental ID to return: ")
                return_date = input("Enter Return Date (YYYY-MM-DD): ")
                self.rental_manager.endRental(rental_id, return_date)
            elif choice == "3":
                # View rented equipment
                self.rental_manager.viewRentals()
            elif choice == "4":
                # Calculate rental cost
                rental_id = input("Enter Rental ID to calculate cost: ")
                self.rental_manager.calculateRental(rental_id)
            elif choice == "5":
                # Return to main menu
                break
            else:
                print("Invalid choice. Please try again.")

    def manageCustomerInfo(self):
        """
            Customer Information Management Menu
        """ 
        while True:
            print("\n=== Manage Customer Info ===")
            print("1. View Customer Information")
            print("2. Add New Customer")
            print("3. Remove Customer")
            print("4. Update Customer Information")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                # View customer information
                self.customer_manager.viewCustomers()
            elif choice == "2":
                # Add a new customer
                customerId = input("Enter Customer ID: ")
                firstname = input("Enter First Name: ")
                lastname = input("Enter Last Name: ")
                contactPhone = input("Enter Contact Phone: ")
                email = input("Enter Email: ")
                notes = input("Enter Notes: ")
                self.customer_manager.addCustomer(customerId, firstname, lastname, contactPhone, email, notes)
            elif choice == "3":
                # Remove a customer
                customerId = input("Enter Customer ID to remove: ")
                self.customer_manager.removeCustomer(customerId)
            elif choice == "4":
                 # Update customer information
                customerId = input("Enter Customer ID to update: ")
                self.customer_manager.editCustomerDetails(customerId)
            elif choice == "5":
                # Return to main menu
                break
            else:
                print("Invalid choice. Please try again.")

    def generateReports(self):
        """
            Report Generation Menu
        """
        while True:
            print("\n=== Generate Reports ===")
            print("1. Report by Date")
            print("2. Report by Customer")
            print("3. Report Equipment by Category")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Generate report by date
                self.report_compilor.reportByDate()
            elif choice == "2":
                # Generate report by customer
                self.report_compilor.reportByCustomer()
            elif choice == "3":
                # Generate report by equipment category
                self.report_compilor.reportEquipmentByCategory()
            elif choice == "4":
                # Return to main menu
                break
            else:
                print("Invalid choice. Please try again.")

    def displayMenu(self):
        """
            MAIN MENU
        """
        while True:
            print("\n=== Main Menu ===")
            print("1. System Manager")
            print("2. Manage Inventory")
            print("3. Equipment Rental")
            print("4. Manage Customer Info")
            print("5. Generate Reports")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.systemManager()
            elif choice == "2":
                self.manageInventory()
            elif choice == "3":
                self.equipmentRental()
            elif choice == "4":
                self.manageCustomerInfo()
            elif choice == "5":
                self.generateReports()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Entry point
    ui = UserInterface()
    try:
        ui.displayMenu()
    finally:
        # Ensuring the database connection is closed
        ui.db.close()
