# a =[1,2,3,4,5,6,7,8,9]
# print(a[2::2])
################################################
# hey = {'1': 1,
#        '2': 2,
#        '3': 3,
#        '4': 4,
#        '5': 5}
# new = {'1': 10, '3': 30}
# hey.update(new)
# a = sum(hey.values())
# print(a)
################################################
# a = [1,2,3]
# print(a[-3:-1])
# a[-3:-1]= 10,20,30,40
# print(a)
################################################
# names1 = ['AMIR', 'BALEY', 'CHALES', 'DAO']
# names2 = [name.lower() for name in names1]
# print(names2[2][2])
#
# print(names1[:])
# print(names1[names1:])
################################################

# Empty tuple
# my_tuple = 1,
# print(type(my_tuple)) # Output: ()

# # set of integers
# my_set = {1, 2, 3}
# print(my_set)
#
# # set of mixed datatypes
# my_set = {1.0, "Hello", (1, 2, 3)}
# print(my_set)

##############################################################################
#
#
# def diagonalDifference(arr):
#     n = 3
#     summ = 0
#     for i in range(n):
#         summ += (arr[i][i] - arr[i][n - 1 - i])
#     return abs(summ)
#
#
# print(diagonalDifference([[1, 4, 5],
#                           [-5, 8, 9],
#                           [-6, 7, 11]]))
# # n = 6
# #
# # for i in range(n):
# #     print(' ' * (n - 1 - i) + '*' * (i + 1))
# students = []
# for i in range(int(input('kac ksi'))):
#     name = input()
#     score = float(input())
#     students.append([name, score])
#
# print(students)
students = [[37.21, 'Harry'], [37.21, 'Berry'], [37.2, 'Tina'], [37.2, 'Tina'], [41, 'Akriti'], [39, 'Harsh']]
score = []
for i in students:
    score.append(i[0])
secondLowestGrade = sorted(list(set(score))).pop(1)
print(secondLowestGrade)
# students.sort()
#
# print(students)
# for i in students:
#     if i[0] == students[1][0]:
#         print(i[1])

# print(students)
# soz = {}
# for i in students:
#     soz[i[0]] = i[1]
# print(soz)
# soz2 = {k: v for k, v in sorted(soz.items(), key=lambda item: item[1])}
# print(soz2)
# soz2.pop()
