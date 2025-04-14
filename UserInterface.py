# Created by Brett Shalagan

from CustomerManager import CustomerManager
from RentalEquipment import RentalEquipment
from RentalEquipmentList import RentalEquipmentList
from RentalManager import RentalManager
from ReportCompilor import ReportCompilor

class UserInterface:
    
    def __init__(self):
        # Creating instances of the necessary classes
        self.report_compilor = ReportCompilor()
        self.customer_manager = CustomerManager()
        self.rental_manager = RentalManager()
        self.rental_equipment = RentalEquipment()
        self.rental_equipment_list = RentalEquipmentList()
        
        
    
    def systemManager(self):
        """
        This method is responsible for managing the system.
        It includes options to add, remove, or update items in the inventory.
        """
        pass
    
    
    
    def manageInventory(self):
        """
        This method is responsible for managing the inventory.
        It includes options to view, add, remove, or update items in the inventory.
        """
        pass
    
    
    
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
    ui.displayMenu()