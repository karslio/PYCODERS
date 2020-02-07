def pythagoras():
    lists = []
    for a in range(3, 98):
        for b in range(a + 1, 99):
            for c in range(b + 1, 100):
                if c * c == b * b + a * a:
                    lists.append((a, b, c))
    return f'(between 1-100) ----->:  {str(lists)[1:-1]}'


print(pythagoras())
