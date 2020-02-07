def counter():
    value = input("enter a value: ")
    upperLetter = smaller = numbrs = others = 0
    for letter in value:
        if letter.isupper():
            upperLetter += 1
        elif letter.islower():
            smaller += 1
        elif letter.isdigit():
            numbrs += 1
        else:
            others += 1
    return f'upper letter: {upperLetter}\nsmaller letter: {smaller}\nnumber: {numbrs}\nothers: {others}'


print(counter())
