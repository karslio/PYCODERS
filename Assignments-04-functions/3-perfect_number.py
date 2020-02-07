def perfect_number():
    lists = []
    for i in range(1, 1001):
        sumDivider = 0
        for j in range(1, i):
            if i % j == 0:
                sumDivider += j
        if sumDivider == i:
            lists.append(i)

    return lists


print(perfect_number())
