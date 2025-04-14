from CustomerManager import CustomerManager
from RentalEquipment import RentalEquipment
from RentalEquipmentList import RentalEquipmentList
from RentalManager import RentalManager

class UserInterface:
    
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
        pass
    
    def manageCustomerInfo(self):
        """
        This method is responsible for managing customer information.
        It includes options to view, add, remove, or update customer information.
        """
        pass
    
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
                self.generateRentalHistoryReport()
            elif choice == "2":
                self.generateInventoryStatusReport()
            elif choice == "3":
                self.generateCustomerInfoReport()
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
            # print(f"DEBUG: User selected option {choice}")

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