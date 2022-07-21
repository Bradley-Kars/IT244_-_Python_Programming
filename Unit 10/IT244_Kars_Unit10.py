import miles
import kilometers
import isfloat
validValue = True
processing = True
while processing:
    print("Enter a number to convert to miles or kilometers:")
    userDistance = (input())
    if isfloat.checkFloat(userDistance):
        userDistance = float(userDistance)
        if userDistance < 0:
            print("Please enter a positive number.")
            validValue = False
        else:
            validValue = True
    else:
        print("Please enter a number.")
        validValue = False
    if validValue:
        print("Enter 'm' to convert to miles or 'k' to convert to kilometers:")
        userUnit = input()
        userUnit = userUnit.lower()
        if userUnit == "m":
            print(str(userDistance) + " kilometers is " + str(miles.convertToMiles(userDistance)) + " miles.")
        elif userUnit == "k":
            print(str(userDistance) + " miles is " + str(kilometers.convertToKilometers(userDistance)) + " kilometers.")
        else:
            print("Please enter 'm' or 'k'.")
    print("Enter 'y' to continue or 'n' to exit:")
    userInput = input()
    if userInput == "y":
        processing = True
    elif userInput == "n":
        processing = False
    else:
        print("Please enter 'y' or 'n'.")