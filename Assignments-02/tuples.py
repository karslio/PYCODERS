#  7.1 - Convert a tuple to a str
# tup1 = ('n', 'e', 't', 'h', 'e', 'r', 'l', 'a', 'n', 'd', 's')
# tupletostring = ''.join(tup1)
# print(tupletostring)

# 7.2 - unzip a list of tuples into individual list and print
# tup2 = [(3, 6), (5, 8), (7, 4)]
# listnew = list(zip(*tup2))
# print(listnew)

# 7.3 - convert a list of tuples into a dictionary and print.
tup3 = [("a", 1), ("a", 2), ("a", 3), ("b", 1), ("b", 2), ("c", 1)]
# A solution
d = dict()

for i in tup3:
    if i[0] in list(d.keys()):
        d[i[0]].append(i[1])
    else:
        d.update({i[0]: [i[1]]})
print(d)
