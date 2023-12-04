while True:
    choice = int(input("Type 1 for USD to PKR, 2 for PKR to USD: "))
    try:
        if choice == 1:
            amount = int(input("Enter your USD amount: "))
            convert = amount*300
            print("Your PKR amount is", convert, "rupees")
        elif choice == 2:
            amount = int(input("Enter you PKR amount: "))
            convert = amount/300
            print("Your USD amount is", convert, "dollars")
        else:
            print("Please enter valid option!")
    except ValueError:
        print("Sorry some error was found")