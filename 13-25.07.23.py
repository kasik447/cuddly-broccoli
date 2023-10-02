# x = 10
# y = 5
# # print(f'{x = }, {y = }')
# # print('x=', x, sep='')
# print(x, 'x', y, '/', 2, '=', x * y / 2)  # 10 x 5 / 2 = 25.0
# print(f'{x} x {y} / 2 = {x * y / 2}')

# num = 74
# print(f'{{{{{num}}}}}')


# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print(r'home' + '\\' + dir_name + '\\' + file_name)


# s = '''Hello
#         world'''
#
# s1 = """Hello
# world"""
#
# '''Комментарий'''
#
# a = 5
# s2 = f"""Hello  !!! {a}
# world"""
#
# print(s)
# print(s1)
# print(s2)


# def square(n):
#     '''Принимает число n, возвращает квадрат числа n'''
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print()
# print(sum.__doc__)
# print()
# print(len.__doc__)


# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительно число, радиус основания цилиндра
#     :param h: положительно число, высота цилиндра
#     :return: положительно число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('A'))
# print(ord('А'))
# print(ord('й'))


# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# s = 'Test string for me'
# arr = [ord(x) for x in s]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое:', arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(1055))


# a = 122
# b = 97
#
# if b > a:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=' ')

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')


# print('apple' > 'Apple')
# print(ord('a'))
# print(ord('A'))


# from random import randint
#
# SHORTEST = 8
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += rand_char
#
#     return res
#
#
# print('Ваш случайный пароль:', random_password())


# s = 'hello, WORLD! I am learning Python!'
# print(s.capitalize())  # Hello, world! i am learning python!
# print(s.lower())  # hello, world! i am learning python!
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON!
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON!
# print(s.title())  # Hello, World! I Am Learning Python!
#
# print(s.count('h', 1, -4))  # кол-во заданных элементов

# print(s.find('Python', 0, 30))  # Возвращает индекс заданного элемента или "-1" - если элемента нет
# print(s.rfind('h'))  # Поиск с конца

# print(s.index('h'))  # Возвращает индекс заданного элемента или ValueError - если элемента нет
# print(s.rindex('h'))  # Поиск с конца


# s1 = 'I am learning Python. hello, WORLD!'
# s1 = s1[:s1.find('h')] + s1[s1.rfind('h') + 1:]
# print(s1)


# s = 'hello, WORLD! I am learning Python!'
# print(s.find('I am'))
# print(s.startswith('I am', 14))  # поиск заданной подстроки с начала, возвращает значение bool
# print(s.endswith('Python!'))  # поиск заданной подстроки с конца, возвращает значение bool


# print('abc123'.isalnum())  # Состоит ли строка из букв и цифр (либо буквы, либо цифры)
# print('ASDnmj'.isalpha())  # Состоит ли строка из букв
# print('123'.isdigit())  # Состоит ли строка из цифр
# print('abc111'.islower())  # Проверяет только буквы на нижний регистр
# print('ASD'.isupper())  # Проверяет только буквы на верхний регистр


# print('py'.center(10, '-'))






