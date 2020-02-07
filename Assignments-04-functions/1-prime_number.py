def isPrime(e):
    if e == 1:
        return False
    elif e == 2:
        return True
    else:
        for i in range(2, e):
            if e % i == 0:  # any of the value is exactly divided the number that is not prime
                return False
        return True


while True:
    number = input('number:')  # we want user input
    if number == 'q':
        break
    else:
        number = int(number)
        if isPrime(number):
            print(number, ' is Prime')
        else:
            print(number, ' is not Prime')

print(isPrime())
