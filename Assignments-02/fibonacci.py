# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
n1 = 0
n2 = 1
fibo = [0]
number = int(input('plese enter a number I will  show you unmtil this number fibonacci numbers'))
while n2 < number:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    fibo.append(n1)
print(tuple(fibo))
