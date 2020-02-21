def greatest_common_divisor(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


print(greatest_common_divisor(30, 45))
