def greatest_common_divisor(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def least_common_multiple():
    y = int(input('enter first number:'))
    x = int(input('enter second number:'))
    return x * y / greatest_common_divisor(x, y)


print(least_common_multiple())
