from datetime import datetime

class RentalManager:
    def __init__(self, equipment_list):
        self.rentals = []
        self.equipment_list = equipment_list

    def addRental(self, rentalId, rentalStartDate, customer, equipment, dailyrentalCost):
        new_rental = {
            'rentalId': rentalId,
            'rentalStartDate': datetime.strptime(rentalStartDate, "%Y-%m-%d"),  # Converting the string to a date
            'customer': customer,
            'equipment': equipment,
            'dailyrentalCost': float(dailyrentalCost),
            'returnDate': None,
            'finalrentalCost': None
        }
        self.rentals.append(new_rental)
        print(f"Rental with ID {rentalId} added successfully.")
        return new_rental

    def endRental(self, rentalId, returnDate):
        for rental in self.rentals:
            if rental['rentalId'] == rentalId:
                rental['returnDate'] = datetime.strptime(returnDate, "%Y-%m-%d")  # Converting the string to date
                daysRented = (rental['returnDate'] - rental['rentalStartDate']).days
                rental['finalrentalCost'] = daysRented * rental['dailyrentalCost']
                print(f"Rental with ID {rentalId} ended. Final cost: ${rental['finalrentalCost']:.2f}")
                return rental
        print(f"No rental found with ID {rentalId}.")

    def removeRental(self, rentalId):
        self.rentals = [rental for rental in self.rentals if rental['rentalId'] != rentalId]
        print(f"Rental with ID {rentalId} has been removed.")

    def viewRentals(self):
        if not self.rentals:
            print("No rentals found.")
        else:
            print("\n=== Current Rentals ===")
            for rental in self.rentals:
                print(f"Rental ID: {rental['rentalId']}, Customer: {rental['customer']}, "
                      f"Equipment: {rental['equipment']}, Start Date: {rental['rentalStartDate'].strftime('%Y-%m-%d')}, "
                      f"Return Date: {rental['returnDate'].strftime('%Y-%m-%d') if rental['returnDate'] else 'N/A'}, "
                      f"Daily Cost: ${rental['dailyrentalCost']:.2f}, "
                      f"Final Cost: ${rental['finalrentalCost'] if rental['finalrentalCost'] else 'N/A'}")
                
    def calculateRental(self, rentalId):
        for rental in self.rentals:
            if rental['rentalId'] == rentalId:
                if rental['returnDate'] is None:
                    print(f"Rental ID {rentalId} has not been returned yet.")
                    return None
                # Calculate the number of days rented
                daysRented = (rental['returnDate'] - rental['rentalStartDate']).days
                # Calculate the final rental cost
                rental['finalrentalCost'] = daysRented * rental['dailyrentalCost']
                print(f"Rental ID {rentalId} calculated. Final cost: ${rental['finalrentalCost']:.2f}")
                return rental['finalrentalCost']
        print(f"No rental found with ID {rentalId}.")
        return None