# Функции
# print()
#
#
# def hello(name, word):  # аргументы
#     print('Hello', word, 'Hello', name)
#
#
# hello('Irina', 'hi')  # параметры
# hello('Ivan', 'hello')
import math

# def get_sum(a, b):
#     print(a + b)
#
#
# n = 2
# m = 3
# get_sum(n, m)
# c = 5
# d = 6
# get_sum(c, d)


# def sumbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# sumbol(9, '+', '-')
# sumbol(7, 'X', '0')


# def get_sum(a, b):
#     print('Текст')
#     return a + b
#
#
# n = 2
# m = 3
# res = get_sum(n, m)
# print(res ** 2)


# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input('a = '))
# b = int(input('b = '))
# m = add(a, b)
# print('Результат:', m)


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()  # последний элемент
#     b = lst.pop(0)  # первый элемент
#     lst.append(b)
#     lst.insert(0, a)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = 5
# b = 2
# if func(a, b):
#     print('Первое число больше второго')
# else:
#     print('Нет')

#
# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False


# print(func(10, 5))
# print(func(5, 10))

# a = 5
# b = 2
# if func(a, b):
#     print('Первое число больше второго')
# else:
#     print('Нет')

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Это надежный пароль')
# else:
#     print('Ненадёжный пароль')


# def get_sum(a, b=2, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# n = 2
# m = 5
# print(get_sum(1, d=n, b=m))


# def set_param(c=20, s='-'):
#     for i in range(c):
#         print(s, end='')
#     print()
#
#
# set_param(10, '+')
# set_param(5, '*')
# set_param(15, '#')
# set_param(7)
# set_param()
# set_param(s='?')


# def digits_sum(n, even=True):  # n = 9874023
#     s = 0
#     while n > 0:
#         cur_digit = n % 10  # 3
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр:')
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print('Сумма нечётных цифр:')
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def display_info(name, age):
#     print('Name', name, '\nAge', age)
#
#
# display_info('Ira', 23)
# display_info(23, 'ira')
# display_info(age=23, name='Ira')


# a = 5
# print(a, id(a))
# a = 6
# print(a, id(a))
#
#
# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.extend([4, 5, 6])
# print(lst1, id(lst1))

# a = 'Hello'
# b = 'Hello'
# a = [1, 2, 3]
# b = [1, 2, 3]
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# Изменяемые типы данных - lst
# Неизменяемые типы данных - int, str, float, bool

# st = 'Hello'
# st = list(st)
# print(st[-1])
# st[-1] = 'q'
# print(st)


# Home_Work

# f1 = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг: '))
#
#
# def rect(h, w):
#     r = h * w
#     return r
#
#
# def triangle(foot, h):
#     t = foot * h // 2
#     return t
#
#
# def circle(r):
#     c = round(math.pi, 2) * (r ** 2)
#     return c
#
#
# if f1 == 1:
#     n1 = int(input('Высота: '))
#     n2 = int(input('Ширина: '))
#     print('Площадь:', rect(n1, n2))
# elif f1 == 2:
#     n3 = int(input('Основание: '))
#     n4 = int(input('Высота: '))
#     print('Площадь:', triangle(n3, n4))
# elif f1 == 3:
#     n5 = int(input('Радиус: '))
#     print('Площадь:', circle(n5))
# else:
#     print('Некорректный ввод данных')






