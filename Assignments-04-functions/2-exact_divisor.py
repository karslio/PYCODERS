def exact_divisor():
    number = int(input('number:'))  # we want user input
    lists = []
    for i in range(1, number + 1):
        if number % i == 0:
            lists.append(i)
    return f'exact divisors of a given number:  {str(lists)[1:-1]}'


print(exact_divisor())
