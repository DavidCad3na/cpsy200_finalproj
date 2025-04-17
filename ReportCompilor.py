#Connor Yasinski
import RentalManager
import RentalEquipmentList

#Class Might need additional options

class ReportCompilor:
    def __init__(self):
        self.report_types = {
            "rental_history": self.generateRentalHistoryReport,
            "inventory_status": self.generateInventoryStatusReport,
            "customer_info": self.generateCustomerInfoReport
        }

    
    def generateRentalHistoryReport(self):
        print("Generating Rental History Report...")
        for rental in RentalManager.rentals:
            print(f"Rental ID: {rental['rentalId']}, Customer: {rental['customer']}, "
                  f"Equipment: {rental['equipment']}, Start Date: {rental['rentalStartDate'].strftime('%Y-%m-%d')}, "
                  f"Return Date: {rental['returnDate'].strftime('%Y-%m-%d') if rental['returnDate'] else 'N/A'}, "
                  f"Daily Cost: ${rental['dailyrentalCost']:.2f}, "
                  f"Final Cost: ${rental['finalrentalCost'] if rental['finalrentalCost'] else 'N/A'}")
        

    def generateInventoryStatusReport(self):
        print("Generating Inventory Status Report...")
        for equipment in RentalEquipmentList.rentalEquipmentList:
            print(f"Equipment ID: {equipment['equipmentId']}, Name: {equipment['name']}, "
                  f"Category: {equipment['category']}, Status: {equipment['status']}, "
                  f"Daily Rental Cost: ${equipment['dailyRentalCost']:.2f}, "
                  f"Quantity Available: {equipment['quantityAvailable']}")

    def generateCustomerInfoReport(self):
        print("Generating Customer Information Report...")
        for customer in RentalManager.customers:
            print(f"Customer ID: {customer['customerId']}, Name: {customer['name']}, "
                  f"Email: {customer['email']}, Phone: {customer['phone']}, "
                  f"Rental History: {len(customer['rentalHistory'])} rentals")
            
    