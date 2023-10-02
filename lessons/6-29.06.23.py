# a = [1, 2, 3]
# b = a.copy()
# print('a =', a, id(a))
# print('b =', b, id(b))
# a.append(20)
# print('a =', a, id(a))
# print('b =', b, id(b))
# b.append(30)
# print('a =', a, id(a))
# print('b =', b, id(b))


# a = [1, 2, 3]
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)


# s = [9, 7, 3, 8, 4, 2, 6]
# s.sort(reverse=True)  # сортировка (по умолчанию - по возрастанию) reverse=True  сортировка по убыванию
# print(s)


# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)
# print(s2)

# s = [9, 7, 3, 8, 4, 2, 6]
# s.sort()
# print(s)
#
# s2 = [9, 7, 3, 8, 4, 2, 6]
# s3 = sorted(s2)
# print(s3)
# print(s2)

# Генерация случайных данных

# import random
# from random import *

# print(random())
# print(randint(5, 9))
# print(randrange(2, 9, 2))  # randrange(start, stop, step)
# print(round(uniform(10.5, 25.5), 2))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(choice(city))
# print(choices(city, k=3))
#
# s = [55, 66, 77, 88, 4, 6, 2, 8, 9, 1]
# # print(choice(s))
# print(choices(s, k=5))


# for i in range(3):
#     print(0)

# from random import randint
#
# a = [randint(50, 100) for i in range(10)]
# print(a)


# lst = [5, 3, 4, 2, 1, 8]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)
# m = max(a)
# print('Max:', m)
# a.remove(m)
# a.insert(0, m)
# print(a)


# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)
# minim = min(a)
# print('Min:', minim)
# ind = a.index(minim)
# print(ind)
# # del a[:ind]
# b = a[ind:]
# print(a)

# x = list('1a2b3c4d')
# print(x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# if not lst:  # len(lst) == 0:
#     print('Список пустой')
#
# print(bool(lst))  # False

# from random import randint
#
# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список:', a)
# print('Второй список:', b)
# c = a + b
# print('Третий список:', c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Третий список:', c)
# c = []
# for i in range(n1):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('Третий список:', c)

# c = [min(a), min(b), max(a), max(b)]
# print('Третий список:', c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print()
# print(len(m))
# print(m[1][2])
# for row in range(len(m)):  # 0 1 2
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# from random import randint

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#     print()

# w, h = 3, 4
# s = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x < 0:
#             s += 1
#         print(x, end='\t\t')
#     print()
# print(s)


# HomeWork

from random import randint

lst = []
n = int(input('Введите размер списка: '))
a = [randint(0, n) for i in range(n)]
b = [randint(0, n) for j in range(n * 10)]
# print(a)

for i in range(len(a)):
    if a[i] not in lst:
        lst.append(a[i])

for j in range(len(b)):
    if b[j] not in lst and len(lst) < n:
        lst.append(b[j])

print('Уникальные случайные числа:', lst)






