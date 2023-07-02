# This is the Tip Calculator
# Add splitting bill
# Add bday bill split
# Add tip

def getCost():
    global total
    individualBill= float(totalBill) / int(totalPeople)
    tipCost = (int(tip) / 100) * float(totalBill)
    total = individualBill + tipCost
    print("----------------------------------------------")
    print("Individual bill: £" + ("%.2f" % total))

def getBdayBill():
    getCost()
    bill = float(bdayBill) / (int(totalPeople)- 1)
    newBill = float(total) + float(bill)
    print("----------------------------------------------")
    print("Birthday bill: £" + str(bdayBill))
    print("Birthday bill split for each person: £" + ("%.2f" % bill)) 
    print("----------------------------------------------")
    print("Individual bill + Birthday Bill: £" + ("%.2f" % newBill))

def menu():
    global totalBill
    global totalPeople
    global tip
    global bdayBill
    print("----------------------------------------------")
    print("Welcome to my tip calculator!")
    totalBill = input("What is the total bill? £")
    totalPeople = input("How many people are you splitting the bill with? ")
    tip = input("How much tip would you like to add (as a percentage)? ")
    print("----------------------------------------------")
    print("Bill: £" + totalBill)
    print("Number of people to split the bill: " + totalPeople)
    print("Tip: " + tip + "%")
    chooseType = input("Do you also need to add a birthday boy/girl's bill to each bill? (Please answer 'Yes' or 'No') ")
    if chooseType == "No":
        getCost()
    else:
        bdayBill = input("How much was the bill for this person? £")
        getBdayBill()
    menu()

menu()