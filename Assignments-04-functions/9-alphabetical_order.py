def alphabetical_order():
    value = input('input values separates the words icon(-) :').split('-')
    value.sort()
    return print('-'.join(value))


alphabetical_order()


# For example: input= green-red-yellow-black-white