# a = list(range(0, 3))
# print(*a)
#
# # listeler

# friends = [1, 2, 3]
# friends2 = []
# print(bool(friends))
# print(bool(friends2))
#
# numbers = [1, 2, 3, 4, 5]
# i = 0
#
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
# transpose = [[row[0] for row in matrix] for i in [0, 1]]
# print(transpose)

# password = ['cckfslkba', 'lkmfwelkm', 'nlkwdnmld', 'abababa', 'dlmdlkm', 'jnklefanlk']
# newList = []
# for i in password:
#     if 'ab' in i or 'ba' in i:
#         newList.append(i)
# print(newList)
#
# newList2 = [i for i in password if 'ab' in i or 'ba' in i]
# print(newList2)

#
# numbers = dict(first=1, second=2)
# sqNumbers = {key: val ** 2 for key, val in numbers.items()}
# print(sqNumbers)


# list1 = ['CA', 'NJ', 'RI']
# list2 = ['california', 'new jersey', 'rhode']
#
# answer = {list1[i]: list2[i] for i in range(len(list1))}
# print(answer)
#
# print(dict(zip(list1, list2)))

# numbers = (1, 2, 3, 4)
# number = (1,)
# values = [20, 30, 40]
# staticValues = tuple(values)
# print(staticValues)
# stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]
# uniqueValues = set(stuff)
# print(uniqueValues)


# liste = ['elie', 'tim', 'matt']
# liste2 = [i[0] for i in liste]
# print(liste2)
#
# liste3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# print([i for i in liste3 if i % 2 == 0])


# firstList = [1, 2, 3, 4]
# # secondList = [3, 4, 5, 6]
# # third = [i for i in firstList if i in secondList]
# # print(third)

# liste = ['Elie', 'Tim', 'Matt']
# liste2 = liste.reverse()
# answer2 = [i[::-1].lower() for i in liste]
# print(answer2)


# answer = [i for i in 'ewoimdwopwqkdkpokwdkwpqokzx,m.,wo;lamazing' if i not in 'aeiou']
# print(answer)


# answer = [[i for i in range(3)] for i in range(3)]
# print(answer)

#
# answer = [[i for i in range(10)] for i in range(10)]
# print(answer)


# numbers = [1, 4, 6, 8, 9, 6, 7, 8, 9, 3, 44, 55, 6,
#            77, 88, 997, 7, 6, 7, 7, 8, 9, 8, 8, 8, 9, 8, 8,
#            0, 9, 0, 9, 8, 9, 8, ]
#
# check = [1, 6, 9, 7]
#
# answer = [i for i in numbers if i in check]
# print(sum(answer)/len(answer))


print({i: chr(i) for i in range(65, 96)})
