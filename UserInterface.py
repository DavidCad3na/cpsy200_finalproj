# Created by Brett Shalagan

from db_manager import DatabaseManager
from CustomerManager import CustomerManager
from RentalEquipment import RentalEquipment
from RentalEquipmentList import RentalEquipmentList
from RentalManager import RentalManager
from ReportCompilor import ReportCompilor

class UserInterface:
    def __init__(self):
        # Creating instances of the necessary classes
        self.db = DatabaseManager()
        self.report_compilor = ReportCompilor()
        self.customer_manager = CustomerManager(self.db)
        self.rental_equipment_list = RentalEquipmentList()  # Initialize RentalEquipmentList first (Must be in this order)
        self.rental_manager = RentalManager(self.rental_equipment_list)  # Pass it to RentalManager (For these 2)
        self.rental_equipment = RentalEquipment()
        
        
    
    def systemManager(self):
        """
        This method is responsible for managing the system.
        It includes options to reset data, view system status, or perform administrative tasks.
        """
        while True:
            print("\n=== System Manager ===")
            print("1. Reset Inventory Data")
            print("2. View System Status")
            print("3. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                confirm = input("Are you sure you want to reset all inventory data? (yes/no): ").strip().lower()
                if confirm == "yes":
                    self.rental_equipment_list.rentalEquipmentList.clear()
                    print("All inventory data has been reset.")
                else:
                    print("Reset operation canceled.")
            elif choice == "2":
                print("\n=== System Status ===")
                print(f"Total Equipment in Inventory: {len(self.db.fetch_query('SELECT * FROM rental_equipment'))}")
                print(f"Total Rentals: {len(self.db.fetch_query('SELECT * FROM rentals'))}")                
                print(f"Total Customers: {len(self.db.fetch_query('SELECT * FROM customers'))}")  # Assuming `customers` is a list in CustomerManager
            elif choice == "3":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    
    
    def manageInventory(self):
        """
        This method is responsible for managing the inventory.
        It includes options to view, add, remove, or update items in the inventory.
        """
        while True:
            print("\n=== Manage Inventory ===")
            print("1. View Inventory")
            print("2. Add New Equipment")
            print("3. Remove Equipment")
            print("4. Update Equipment Availability")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.rental_equipment_list.viewRentalEquipment()
            elif choice == "2":
                equipment_id = input("Enter Equipment ID: ")
                name = input("Enter Equipment Name: ")
                available = input("Is the equipment available? (yes/no): ").strip().lower() == "yes"
                self.rental_equipment_list.addRentalEquipment({
                    'equipmentId': equipment_id,
                    'name': name,
                    'available': available
                })
            elif choice == "3":
                equipment_id = input("Enter Equipment ID to remove: ")
                self.rental_equipment_list.removeRentalEquipment(equipment_id)
            elif choice == "4":
                equipment_id = input("Enter Equipment ID to update availability: ")
                availability = input("Is the equipment available? (yes/no): ").strip().lower() == "yes"
                if availability:
                    self.rental_equipment_list.markAsReturned(equipment_id)
                else:
                    self.rental_equipment_list.markAsRented(equipment_id)
            elif choice == "5":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    
    
    def equipmentRental(self):
        """
        This method is responsible for managing equipment rentals.
        It includes options to rent, return, or view rented equipment.
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
                rental_id = input("Enter Rental ID: ")
                rental_start_date = input("Enter Rental Start Date (YYYY-MM-DD): ")
                customer = input("Enter Customer Name: ")
                equipment = input("Enter Equipment Name: ")
                daily_rental_cost = input("Enter Daily Rental Cost: ")
                self.rental_manager.addRental(rental_id, rental_start_date, customer, equipment, daily_rental_cost)
            elif choice == "2":
                rental_id = input("Enter Rental ID to return: ")
                return_date = input("Enter Return Date (YYYY-MM-DD): ")
                self.rental_manager.endRental(rental_id, return_date)
            elif choice == "3":
                self.rental_manager.viewRentals()
            elif choice == "4":
                rental_id = input("Enter Rental ID to calculate cost: ")
                self.rental_manager.calculateRental(rental_id)
            elif choice == "5":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
        
    
    
    def manageCustomerInfo(self):
        """
        This method is responsible for managing customer information.
        It includes options to view, add, remove, or update customer information.
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
                self.customer_manager.viewCustomers()
            elif choice == "2":
                customerId = input("Enter Customer ID: ")
                firstname = input("Enter First Name: ")
                lastname = input("Enter Last Name: ")
                contactPhone = input("Enter Contact Phone: ")
                email = input("Enter Email: ")
                notes = input("Enter Notes: ")
                self.customer_manager.addCustomer(customerId, firstname, lastname, contactPhone, email, notes)
            elif choice == "3":
                customerId = input("Enter Customer ID to remove: ")
                self.customer_manager.removeCustomer(customerId)
            elif choice == "4":
                customerId = input("Enter Customer ID to update: ")
                self.customer_manager.editCustomerDetails(customerId)
            elif choice == "5":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
                
    
    
    def generateReports(self):
        """
        This method is responsible for generating reports.
        It includes options to view rental history, inventory status, and customer information.
        """
        while True:
            print("\n=== Generate Reports ===")
            print("1. Rental History Report")
            print("2. Inventory Status Report")
            print("3. Customer Information Report")
            print("4. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.report_compilor.generateRentalHistoryReport()
            elif choice == "2":
                self.report_compilor.generateInventoryStatusReport()
            elif choice == "3":
                self.report_compilor.generateCustomerInfoReport()
            elif choice == "4":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
                
                
        
    def displayMenu(self):
        """
        This method displays the main menu of the application.
        It includes options to navigate to different sections of the application.
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
            # print(f"DEBUG: User selected option {choice}") (In the case option selection starts buggin try this)

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
                
                

# Entry point for the program
if __name__ == "__main__":
    ui = UserInterface()
    try:
        ui.displayMenu()
    finally:
        ui.db.close()