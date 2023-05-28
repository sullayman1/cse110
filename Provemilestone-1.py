childprice = input("What is the price of a child's meal? ")
print()
adultprice = input("What is the price of an adult's meal? ")
print()
childtotal = input("How many children are there? ")
print()
adultstotal = input("How many adults are there? ")
print()
taxtotal = input("What is the sales tax rate? ")
print()
amountmoney = input("What is the payment amount? ")
print()

#step2: processing
childprice = adultprice + childtotal + adultstotal + taxtotal * amountmoney
print()
