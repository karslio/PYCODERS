lists = []
print("to stop the program please enter 'q'")
while True:
    value = input("Enter list element as a number: ")
    if value == 'q':
        break
    else:
        lists.append(value)
print(lists)
maxRepetedElement = (max(set(lists), key=lists.count))

print(
    f'Max distance between the maximum repetad number ({maxRepetedElement}) is'
    f' {len(lists) - 1 - lists[::-1].index(maxRepetedElement) - lists.index(maxRepetedElement)}')
