def greatest_common_divisor():
    y = int(input('enter first number:'))
    x = int(input('enter second number:'))
    while y != 0:
        (x, y) = (y, x % y)
    return x


print(greatest_common_divisor())
