print("Welcome to The Ice Creamery")
print()
flavorsList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]
flavorsList[6] = "Cotton Candy"
flavorsList.append("Bubble Gum")
flavorsList.sort()
flavorsCount = len(flavorsList)
for i in range(len(flavorsList)):
    print ("Flavor #:", i+1, end = " ")
    print (flavorsList[i])
print()
conePrices={"S":"$1.50","M":"$2.50","L":"$3.50"}
coneSizes={"S":"Small","M":"Medium","L":"Large"}
customerSize=str(input("Please enter the cone size of your choosing: S, M, or L: ")).upper()
if customerSize in coneSizes:
    pass
else:
    print("Not a valid selection")
    exit()
print()
customerFlavor=int(input("Please enter your flavor number: "))
if 0<customerFlavor<=len(flavorsList):
    pass
else:
    print("Not a valid selection")
    exit()
print()
print("Your total is:", conePrices[customerSize])
print("Your", coneSizes[customerSize], "sized cone of The Ice Creamery's", flavorsList[customerFlavor-1], "will arrive shortly.")
print()
print("Thank you for visiting the Ice Creamery!")