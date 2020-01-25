lists = []
print("to stop the program please enter 'q'")
xthSmallest = int(input("Which number do you want to know as Xth smallest number in the list?"))
while True:
    value = input("Enter number: ")
    if value == 'q':
        break
    else:
        lists.append(int(value))
lists.sort()
print(f'{xthSmallest}th smallest element in the given list is {lists[xthSmallest-1]}.')
