#import rentalEquipment as re
rentalEquipmentList = []

def addRentalEquipment(equipment):
    rentalEquipmentList.append(equipment)
    return equipment

def removeRentalEquipment(equipmentId):
    global rentalEquipmentList
    rentalEquipmentList = [equipment for equipment in rentalEquipmentList if equipment['equipmentId'] != equipmentId]
    print(f"Rental equipment with ID {equipmentId} has been removed.")

def viewRentalEquipment():
    global rentalEquipmentList
    return rentalEquipmentList