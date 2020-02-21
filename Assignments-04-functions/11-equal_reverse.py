def equal_reverse():
    word = input('enter a word')
    newString = word[::-1]
    if word == newString:
        return True
    else:
        return False


print(equal_reverse())

# Ex: madam, tacocat, utrecht
# Result: True, True, False
