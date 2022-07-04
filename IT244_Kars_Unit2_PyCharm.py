# coding=utf-8
print("Your color choices are red, blue, green, white or yellow.")
userColor = raw_input("Enter a color from the list above: ")
color = userColor.lower()
validColor = True
if color == 'red':
        spanishColor = 'rojo'
elif color == 'blue':
        spanishColor = "azule"
elif color == 'green':
        spanishColor = "verde"
elif color == 'white':
        spanishColor = "blanco"
elif color == 'yellow':
        spanishColor = "amarillo"
else:
        validColor = False
if validColor:
    print("The color", color, "in Spanish is " + spanishColor)
else:
    print("That is not a valid color for this program. Ese no es un color válido")