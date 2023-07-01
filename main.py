# This is the Tip Calculator
# Add splitting bill
# Add bday bill split
# Add tip

def menu():
    print("Welcome to my tip calculator!")
    totalBill = input("What is the total bill? £")
    totalPeople = input("How many people are you splitting the bill with? ")
    tip = input("How much tip would you like to add? ")
    print("Bill: £" + totalBill)
    print("Number of people to split the bill: " + totalPeople)
    print("Tip " + tip + "%")
    menu()

menu()