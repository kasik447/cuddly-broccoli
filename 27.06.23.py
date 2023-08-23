# import math
#
#
# num1 = math.sqrt(4)  # корень
# num2 = math.ceil(3.2)  # округ в большую сторону
# num3 = math.floor(3.8)  # округ в меньшую сторону
# num4 = math.pi
# print(num1)
# print(num2)
# print(num3)
# print(num4)


# import math as m
#
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
#
# print(num2)
# print(num3)


# from math import ceil, floor
#
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num2)
# print(num3)


# from math import *
#
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num2)
# print(num3)

# import time

# sec = time.time()
# print(sec)
# local = time.ctime(24338)
# print(local)
# res = time.localtime()
# print(res)
# print(res.tm_year)

# import time
# import locale

# locale.setlocale(locale.LC_ALL, 'ru')

# print(time.strftime('Сегодня %B %d, %Y', time.localtime(24338)))
# print(time.strftime('%d/%m/%Y, %H:%M:%S'))

# print('Программа запустилась...')
# time.sleep(5)
# print('Программа завершилась')

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print('Время выполнения программы', finish - start, 'секунд')

# Срезы: список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# a = s[4:0:-1]
# print(a)

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1:7:2])
# print(s[0:1])
# print(s[6:7])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3:5] = []
# print(s)
# del s[:]
# print(s)
# Методы списков
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([8, 9, 10])  # добавляет в список итерируемый объект (несколько элементов)
# print(s)
# s.extend('add')
# print(s)
# s.insert(5, 100)  # Добавляет элемент в список, первый параметр - индекс, второй параметр - добавляемое значение.
# print(s)

# s = []
# n = int(input('Кол-во элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     s.insert(0, x)
# print(s)

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)

# s = []
# n = int(input('Кол-во элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка.')
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)  # [2, 1, 4, 3]

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3,5)
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3,5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3,5)
#         c.append(a[i])
# print(c)

# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# s.remove(0)  # удаляет первый найденный элемент из списка по заданному значению
# print(s)
#
# last = s.pop()  # удаляет последний элемент из списка и вернул удаляемое значение
# print(last)
# print(s)
#
# last = s.pop(0)  # удаляет последний элемент по заданному индексу
# print(last)
# print(s)
#
# s.clear()  # очищает список
# print(s)


# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# print('Введите индекс: ')
# k = int(input('k = '))
# a.pop(k)
# print(a)

# s = [4, 0, 2, 0, 3, 6, 0, 0, 7]
# print(s)
# num = s.count(0)  # считает количество заданных элементов в списке
# print(num)
# ind = s.index(0, 2)  # возвращает индекс первого найденного элемента по его значению, если значения нет ValueError
# print(ind)


# HomeWork
# p = []
# a = [0] * int(input('Введите длину списка: '))
#
# for i in range(len(a)):
#     a[i] = int(input('Введите элемент списка: '))
#     if a[i] >= 0:
#         p.append(a[i])
# print('Список:', a)
# print('Новый список, состоящий из положительный элементов:', p)
#
# max1 = p[0]
# for j in p:
#     if j > max1:
#         max1 = j
# print('Наибольший элемент списка:', max1)







