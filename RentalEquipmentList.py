# Created by David Cadena / Altered By Brett Shalagan

class RentalEquipmentList:
    def __init__(self, db):
        self.db = db

    def addRentalEquipment(self, equipment):
        query = """
        INSERT INTO rental_equipment (equipmentId, name, available, categoryId)
        VALUES (%s, %s, 1, %s)
        """
        self.db.execute_query(query, (
            equipment['equipmentId'],
            equipment['name'],
            equipment['categoryId'] 
        ))
        print(f"Equipment {equipment['name']} with ID {equipment['equipmentId']} added successfully.")
        return equipment


    def removeRentalEquipment(self, equipmentId):
        query = "DELETE FROM rental_equipment WHERE equipmentId = %s"
        self.db.execute_query(query, (equipmentId,))
        print(f"Rental equipment with ID {equipmentId} has been removed.")

    def viewRentalEquipment(self):
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
        query = "SELECT available FROM rental_equipment WHERE equipmentId = %s"
        result = self.db.fetch_query(query, (equipmentId,))
        if result:
            if result[0][0] == 1:
                print(f"Equipment with ID {equipmentId} is available.")
                return True
            else:
                print(f"Equipment with ID {equipmentId} is not available.")
                return False
        else:
            print(f"Equipment with ID {equipmentId} not found.")
            return False

    def markAsRented(self, equipmentId):
        query = "UPDATE rental_equipment SET available = 0 WHERE equipmentId = %s"
        self.db.execute_query(query, (equipmentId,))
        print(f"Equipment ID {equipmentId} marked as rented.")
        return True

    def markAsReturned(self, equipmentId):
        query = "UPDATE rental_equipment SET available = 1 WHERE equipmentId = %s"
        self.db.execute_query(query, (equipmentId,))
        print(f"Equipment ID {equipmentId} marked as available.")
        return True
