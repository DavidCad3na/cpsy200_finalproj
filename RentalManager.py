rental = []
rentalId = ""
rentalStartDate = ""
returnDate = ""
customer = ""
equipment = ""
dailyrentalCost = 0.0
finalrentalCost = 0.0

def endRental(rentalId, returnDate):
    global rental, finalrentalCost
    for r in rental:
        if r['rentalId'] == rentalId:
            r['returnDate'] = returnDate
            daysRented = (returnDate - r['rentalStartDate']).days
            finalrentalCost = daysRented * r['dailyrentalCost']
            r['finalrentalCost'] = finalrentalCost
            break

def addRental(rentalId, rentalStartDate, customer, equipment, dailyrentalCost):
    global rental
    new_rental = {
        'rentalId': rentalId,
        'rentalStartDate': rentalStartDate,
        'customer': customer,
        'equipment': equipment,
        'dailyrentalCost': dailyrentalCost,
        'returnDate': None,
        'finalrentalCost': None
    }
    rental.append(new_rental)
    return new_rental

def removeRental(rentalId):
    global rental
    rental = [r for r in rental if r['rentalId'] != rentalId]
    print(f"Rental with ID {rentalId} has been removed.")

def viewRentals():
    global rental
    return rental

def viewRentalsFormatted():
    global rental
    formatted_rentals = ""
    for r in rental:
        formatted_rentals += f"""
        Rental ID: {r['rentalId']}
        Start Date: {r['rentalStartDate']}
        Customer: {r['customer']}
        Equipment: {r['equipment']}
        Daily Cost: ${r['dailyrentalCost']:.2f}
        Return Date: {r['returnDate']}
        Final Cost: ${r['finalrentalCost'] if r['finalrentalCost'] is not None else 'N/A'}"""
    return formatted_rentals

def calculateRental(rentalId):
    global rental, finalrentalCost
    for r in rental:
        if r['rentalId'] == rentalId:
            daysRented = (r['returnDate'] - r['rentalStartDate']).days
            finalrentalCost = daysRented * r['dailyrentalCost']
            return finalrentalCost