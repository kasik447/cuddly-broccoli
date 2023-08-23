# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: (s > 75) and s < 80, b))
# print(res)

#  Декоратор

# def hello():
#     return 'Hello "hello"'
#
#
# def super_func(func):
#     print('Hello "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello "hello"'
#
#
# print(id(hello))
# test = hello
# print(id(test))
# print(test())


# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print('Hello "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # Декорирующая функция
#     def wrap():
#         print('*' * 20)
#         func()
#         print('=' * 20)
#     return wrap
#
#
# @my_decorator  # Декоратор
# def func_test():  # Декорируемая функция
#     print('Hello "func_test"')
#
# @my_decorator
# def hello():
#     print('Hello "hello"')
#
#
#
# func_test()
# hello()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())


# def cnt(fn):
#     c = 0
#
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print('Вызов функции:', c)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', 'Резникова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_full_name('Борис', 'Елизавета', 'Светлана', study='JavaScript')
# print_full_name('Владимир', 'Екатерина', 'Виктор')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность:', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(arg):  # 3
#     def outer(func):  # return_num
#         def wrap(*args, **kwargs):  # num
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_arg, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_arg[i]) != args[i]:
#                     raise TypeError('Неверный тип данных')
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError('Неверный тип данных', f_kwargs[k])
#
#             return fn(*f_arg, **f_kwargs)
#         return wrap
#     return outer
#
#
# @typed(int, int, int)
# def type_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def type_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def type_fn3(x, y, z='Hello'):
#     return (x + y) * z
#
#
# print(type_fn(3, 4, 5))
# # print(type_fn(3, 4, '!'))
#
# print(type_fn2('Hello', 'wold', '!'))
# # print(type_fn2(6, 4, 2))
#
# print(type_fn3('Hello', 'wold', z='5'))


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010)
# print(0b10010 + 0o22)
# print(0o22)
# print(0x12)


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print('t' in e)
# print(e[1])
# print(e[1: -1])
# print(e[1: -1:2])
# print(e[:])
# print(e[::-1])


# print('Привет')
# print(u'Привет')


# print('C:\\folder\\file.txt')
# print(r'C:\folder\file.txt')
#
# print(r'C:\folder\file.txt\\'[:-1])
# print(r'C:\folder\file.txt' + '\\')
# print('C:\\folder\\file.txt\\')

# name = 'Дмитрий'
# age = 25
# print('Меня зовут ', name, '. Мне ', age, ' лет ', sep='')
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет ')
# print(f'Меня зовут {name}. Мне {age} лет')


# print(f'Число: {round(10 / 3, 2)}')
# print(f'Число: {10 / 3:.2f}')




