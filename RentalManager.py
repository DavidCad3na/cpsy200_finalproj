# Created by David Cadena / Altered by Heet Talati

from datetime import datetime
import RentalEquipmentList

class RentalManager:
    def __init__(self, db, equipment_list):
        self.db = db
        self.equipment_list = equipment_list

    def addRental(self, rentalId, rentalStartDate, customer, equipment_id,rentalCost):
        query = """
        INSERT INTO rentals (rentalId, rentalStartDate, customer, equipment_id, rentalCost)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (rentalId, rentalStartDate, customer, equipment_id,float(rentalCost)))
        if RentalEquipmentList.isEquipmentAvailable(self, equipment_id):
            RentalEquipmentList.markAsRented(self, equipment_id)
            print(f"Rental with ID {rentalId} added successfully.")
        else:
            print(f"Equipment with ID {equipment_id} is not available for rental.")

    def endRental(self, rentalId, returnDate):
        query = "SELECT rentalStartDate, dailyRentalCost, equipment_id FROM rentals WHERE rentalId = %s"
        result = self.db.fetch_query(query, (rentalId,))

        if not result:
            print(f"No rental found with ID {rentalId}.")
            return

        rentalStartDate, dailyRentalCost, equipment_id = result[0]

        # Ensure rentalStartDate is a datetime.date object
        if isinstance(rentalStartDate, datetime):
            rentalStartDate = rentalStartDate.date()

        # Convert returnDate to a datetime.date object
        returnDate_obj = datetime.strptime(returnDate, "%Y-%m-%d").date()

        # Calculate the number of days rented
        daysRented = (returnDate_obj - rentalStartDate).days
        finalRentalCost = daysRented * dailyRentalCost

        update_query = """
        UPDATE rentals
        SET returnDate = %s, finalRentalCost = %s
        WHERE rentalId = %s
        """
        self.db.execute_query(update_query, (returnDate, finalRentalCost, rentalId))

        # Mark the equipment as returned
        self.equipment_list.markAsReturned(equipment_id)
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
