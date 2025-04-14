from RentalManager import RentalManager
from RentalEquipmentList import RentalEquipmentList

class Main:

    # Initialize the equipment list
    equipment_list = RentalEquipmentList()

    # Add some equipment to the inventory
    equipment_list.addRentalEquipment({'equipmentId': 'E001', 'name': 'Excavator', 'available': True})
    equipment_list.addRentalEquipment({'equipmentId': 'E002', 'name': 'Bulldozer', 'available': True})

    # Initialize the rental manager with the equipment list
    rental_manager = RentalManager(equipment_list)