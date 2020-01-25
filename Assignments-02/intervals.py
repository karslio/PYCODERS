alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# intervals = {key: tuple(range(i, i + 10)) for i in range(0, 10) for key in alphabet}
a = 0
intervals = {}
for i in alphabet:
    intervals[i] = tuple(range(a+1, a + 11))
    a += 10
print(intervals)