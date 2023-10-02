# n = int(input('Введите количество ворон (0-9): '))
# if 0 <= n <= 9:
#     print('На ветке', end=' ')
#     if n == 1:
#         print(n, 'ворона')
#     elif 2 <= n <= 4:
#         print(n, 'вороны')
#     else:
#         print(n, 'ворон')
# else:
#     print('Ошибка ввода данных')

# password = 'admin'
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')

# day = 'Понедельник'
# time = 14
#
# match day:
#     case 'Понедельник' | 'Вторник' | 'Среда' | 'Четверг' | 'Пятница' if 9 <= time <= 16:
#         print('Рабочий день')
#     case 'Суббота' | 'Воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует или не рабочее время')

# Тернарное выражение

# a, b = 10, 20
# minim = a if a < b else b
# print(minim)

# a, b = 30, 20
# print('a == b' if a == b else 'a > b' if a > b else 'b < a')

# a, b = 4, 2
# print('На ноль делить нельзя' if b == 0 else a / b)

# try:  # попытаться
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:  # Исключение
#     print('Что-то пошло не так')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print('Нельзя делить на 0')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки. Нельзя делить на 0')
# else:  # Когда в блоке try не возникло исключение
#     print('Всё нормально. Вы ввели числа', n, 'и', m)
# finally:  # Выводится в любом случае
#     print('Конец программы')

# n = (input('Введите первое число: '))
# m = (input('Введите второе число: '))
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print('i =', i)
#     i += 1

#  итерация - один шаг цикла

# i = 10
# while i > 0:
#     print('i =', i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 1

# n = int(input('Укажите количество символов: '))
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1
# while n > 0:
#     print('*', end='')
#     n -= 1
# print('*' * n)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# res = 0
# while a <= b:
#     if a % 2:  # a % 2 != 0:
#         res += a
#     a += 1
# print('Сумма целых нечетных чисел:', res)

# n = input('Введите целое число: ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Чётное')
# else:
#     print('Нечётное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершён')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

































