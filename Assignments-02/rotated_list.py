listElements = []
slip = int(input("how many index you will slip left"))
print("to stop the program please enter 'q'")
while True:
    value = input("Enter list element: ").lower()
    if value == 'q':
        break
    else:
        listElements.append(value)
print(listElements)
newList = listElements[slip:] + listElements[:slip]
print("The new order of list is: " + " ".join(map(str, newList)))
