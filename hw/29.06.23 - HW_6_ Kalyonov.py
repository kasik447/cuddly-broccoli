# HomeWork

from random import randint

lst = []
n = int(input('Введите размер списка: '))
a = [randint(0, n) for i in range(n)]
b = [randint(0, n) for j in range(n * 10)]

for i in range(len(a)):
    if a[i] not in lst:
        lst.append(a[i])

for j in range(len(b)):
    if b[j] not in lst and len(lst) < n:
        lst.append(b[j])

print('Уникальные случайные числа:', lst)
