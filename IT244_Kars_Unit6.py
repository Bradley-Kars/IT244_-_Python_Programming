def convertTemp():
    global temps
    if str(tempScale) in ['f','F']:
        temps[0] = ((int(temps[1]) - 32) * 5/9)
    elif str(tempScale) in ['c','C']:
        temps[1] = ((int(temps[0]) * 9/5) + 32)
    else:
        print("invalid entry")
        exit()
temps = list(('0','0'))
tempEntered = float(input("Enter a temperature value: "))
print()
tempScale = input("Enter a single letter to indicate the temperature scale (C or F): ")
if str(tempScale) in ['f','F']:
    temps[1] = tempEntered
elif str(tempScale) in ['c','C']:
    temps[0] = tempEntered
convertTemp()
print()
print("You entered", tempEntered,"degrees", tempScale.upper(), ">>>","\n")
print("The temperature in Celsius is", temps[0],"\n")
print("The temperature in Fahrenheit is", temps[1])