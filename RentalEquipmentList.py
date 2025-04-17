# Created by David Cadena / Altered By Brett Shalagan

class RentalEquipmentList:
    def __init__(self, db):
        # Accept a database connection wrapper
        self.db = db

    def addRentalEquipment(self, equipment):
        """
        Adds a new piece of equipment to the database.
        """
        query = """
        INSERT INTO rental_equipment (equipmentId, name, available)
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(query, (equipment['equipmentId'], equipment['name'], equipment['available']))
        print(f"Equipment {equipment['name']} with ID {equipment['equipmentId']} added successfully.")
        return equipment

    def removeRentalEquipment(self, equipmentId):
        """
        Removes a piece of equipment from the database by ID.
        """
        query = "DELETE FROM rental_equipment WHERE equipmentId = %s"
        self.db.execute_query(query, (equipmentId,))
        print(f"Rental equipment with ID {equipmentId} has been removed.")

    def viewRentalEquipment(self):
        """
        Returns and prints the list of all rental equipment from the database.
        """
        query = "SELECT * FROM rental_equipment"
        results = self.db.fetch_query(query)

        if not results:
            print("No rental equipment available.")
        else:
            print("\n=== Rental Equipment List ===")
            for equipment in results:
                print(f"ID: {equipment[0]}, Name: {equipment[1]}, Available: {equipment[2]}")
        return results

    def isEquipmentAvailable(self, equipmentId):
        """
        Checks if a piece of equipment is available for rent.
        """
        query = "SELECT available FROM rental_equipment WHERE equipmentId = %s"
        result = self.db.fetch_query(query, (equipmentId,))
        if result:
            return result[0][0]
        print(f"Equipment with ID {equipmentId} not found.")
        return False

    def markAsRented(self, equipmentId):
        """
        Marks a piece of equipment as rented (unavailable).
        """
        query = "UPDATE rental_equipment SET available = FALSE WHERE equipmentId = %s"
        self.db.execute_query(query, (equipmentId,))
        print(f"Equipment ID {equipmentId} marked as rented.")
        return True

    def markAsReturned(self, equipmentId):
        """
        Marks a piece of equipment as returned (available).
        """
        query = "UPDATE rental_equipment SET available = TRUE WHERE equipmentId = %s"
        self.db.execute_query(query, (equipmentId,))
        print(f"Equipment ID {equipmentId} marked as available.")
        return True