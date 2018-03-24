
def vendingMachine ():
    count = 0
    totalCredit = 0
    coinNum = int (input ("How many coins would you like to enter: "))
    while count in range (coinNum):
        coin = float (input ("Enter coin: $ " ))
        totalCredit = totalCredit + coin
        count = count + 1
    print ("You have ${0} in your bank.".format (round(totalCredit, 2)))
    print ("Choose your item:")
    print ("")
    print ("1. 60 Minutes Ticket (1.20$)")
    print ("2. 1 Day Ticket (3.00$)")
    print ("3. 7 Days Ticket (10.0$)")
    print ("")
    finalCredit = totalCredit
    round (finalCredit, 2)
    item = int (input("Enter the number for your ticket : "))
    while item <1 or item >3:
        print("Ticket number not available.")
        item = int (input ("Enter the number for your ticket : "))
    if totalCredit < 1.20:
        print ("")
        print ("INSERT more coins")
    elif item == 1:
        finalCredit = totalCredit - 1.20
        print ("You have now a 60 minutes Ticket, costing 1.20$.")
        print ("")
        print ("You have {0} remaining in your bank.".format (round(finalCredit,2)))

    elif item == 2 and totalCredit > 2.99:
        finalCredit = totalCredit - 3.00
        print ("You have now a 1 Day Ticket, costing 3.00$.")
        print ("")
        print ("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    elif item == 3 and totalCredit > 9.99:
        finalCredit = totalCredit - 10.0
        print ("You have now a 7 Days Ticket, costing 10.0$.")
        print ("")
        print ("You have {0} remaining in your bank.".format (round(finalCredit,2)))
    if item <1 or item >3:
        print ("This is not an option.")
    print ("")
    print ("Please COLLECT the rest of your money : ${0}".format(round(finalCredit,2)))

vendingMachine ()

