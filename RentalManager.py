# Created by David Cadena / Altered by Heet Talati

from datetime import datetime

class RentalManager:
    def __init__(self, db, equipment_list):
        self.db = db
        self.equipment_list = equipment_list

    def addRental(self, rentalId, rentalStartDate, customer, equipment, dailyrentalCost):
        query = """
        INSERT INTO rentals (rentalId, rentalStartDate, customer, equipment, dailyRentalCost)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (rentalId, rentalStartDate, customer, equipment, float(dailyrentalCost)))
        print(f"Rental with ID {rentalId} added successfully.")

    def endRental(self, rentalId, returnDate):
        # Fetch rentalStartDate and dailyRentalCost for calculation
        query = "SELECT rentalStartDate, dailyRentalCost FROM rentals WHERE rentalId = %s"
        result = self.db.fetch_query(query, (rentalId,))

        if not result:
            print(f"No rental found with ID {rentalId}.")
            return

        rentalStartDate, dailyRentalCost = result[0]
        rentalStartDate = rentalStartDate  # datetime from DB
        returnDate_obj = datetime.strptime(returnDate, "%Y-%m-%d")
        daysRented = (returnDate_obj - rentalStartDate).days
        finalRentalCost = daysRented * dailyRentalCost

        update_query = """
        UPDATE rentals
        SET returnDate = %s, finalRentalCost = %s
        WHERE rentalId = %s
        """
        self.db.execute_query(update_query, (returnDate, finalRentalCost, rentalId))
        print(f"Rental with ID {rentalId} ended. Final cost: ${finalRentalCost:.2f}")

    def removeRental(self, rentalId):
        query = "DELETE FROM rentals WHERE rentalId = %s"
        self.db.execute_query(query, (rentalId,))
        print(f"Rental with ID {rentalId} has been removed.")

    def viewRentals(self):
        query = "SELECT * FROM rentals"
        rentals = self.db.fetch_query(query)

        if not rentals:
            print("No rentals found.")
        else:
            print("\n=== Current Rentals ===")
            for rental in rentals:
                rentalId, rentalStartDate, returnDate, customer, equipment, dailyRentalCost, finalRentalCost = rental
                print(f"Rental ID: {rentalId}, Customer: {customer}, Equipment: {equipment}, "
                      f"Start Date: {rentalStartDate.strftime('%Y-%m-%d') if rentalStartDate else 'N/A'}, "
                      f"Return Date: {returnDate.strftime('%Y-%m-%d') if returnDate else 'N/A'}, "
                      f"Daily Cost: ${dailyRentalCost:.2f}, "
                      f"Final Cost: ${finalRentalCost if finalRentalCost is not None else 'N/A'}")

    def calculateRental(self, rentalId):
        query = "SELECT rentalStartDate, returnDate, dailyRentalCost FROM rentals WHERE rentalId = %s"
        result = self.db.fetch_query(query, (rentalId,))

        if not result:
            print(f"No rental found with ID {rentalId}.")
            return None

        rentalStartDate, returnDate, dailyRentalCost = result[0]

        if returnDate is None:
            print(f"Rental ID {rentalId} has not been returned yet.")
            return None

        daysRented = (returnDate - rentalStartDate).days
        finalRentalCost = daysRented * dailyRentalCost

        print(f"Rental ID {rentalId} calculated. Final cost: ${finalRentalCost:.2f}")
        return finalRentalCost
