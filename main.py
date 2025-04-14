class Main:

    import RentalManager as rm

    #Test code for RentalManager
    print("Final CSPY project for semester 2")
    rm.addRental("R001", "2025-04-14", "Dave Doe", "Snow Board", 25.0)
    print("Rental added successfully.")
    print(rm.viewRentalsFormatted())