# Created by David Cadena / Altered By Brett Shalagan

class RentalEquipmentList:
    def __init__(self):
        # Initialize the equipment list as an instance variable
        self.rentalEquipmentList = []

    def addRentalEquipment(self, equipment):
        """
        Adds a new piece of equipment to the rental equipment list.
        """
        self.rentalEquipmentList.append(equipment)
        print(f"Equipment {equipment['name']} with ID {equipment['equipmentId']} added successfully.")
        return equipment

    def removeRentalEquipment(self, equipmentId):
        """
        Removes a piece of equipment from the rental equipment list by its ID.
        """
        self.rentalEquipmentList = [
            equipment for equipment in self.rentalEquipmentList if equipment['equipmentId'] != equipmentId
        ]
        print(f"Rental equipment with ID {equipmentId} has been removed.")

    def viewRentalEquipment(self):
        """
        Returns the list of all rental equipment.
        """
        if not self.rentalEquipmentList:
            print("No rental equipment available.")
        else:
            print("\n=== Rental Equipment List ===")
            for equipment in self.rentalEquipmentList:
                print(f"ID: {equipment['equipmentId']}, Name: {equipment['name']}, Available: {equipment['available']}")
        return self.rentalEquipmentList

    def isEquipmentAvailable(self, equipmentId):
        """
        Checks if a piece of equipment is available for rent.
        """
        for equipment in self.rentalEquipmentList:
            if equipment['equipmentId'] == equipmentId:
                return equipment['available']
        print(f"Equipment with ID {equipmentId} not found.")
        return False

    def markAsRented(self, equipmentId):
        """
        Marks a piece of equipment as rented (unavailable).
        """
        for equipment in self.rentalEquipmentList:
            if equipment['equipmentId'] == equipmentId:
                equipment['available'] = False
                print(f"Equipment ID {equipmentId} marked as rented.")
                return True
        print(f"Equipment ID {equipmentId} not found.")
        return False

    def markAsReturned(self, equipmentId):
        """
        Marks a piece of equipment as returned (available).
        """
        for equipment in self.rentalEquipmentList:
            if equipment['equipmentId'] == equipmentId:
                equipment['available'] = True
                print(f"Equipment ID {equipmentId} marked as available.")
                return True
        print(f"Equipment ID {equipmentId} not found.")
        return False