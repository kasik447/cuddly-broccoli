# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# s = dict()
# n = None
#
# for i in a:
#     if type(i) == str:
#         s[i] = []
#         n = i
#     else:
#         s[n].append(i)
#
# print(s)


# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# s = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# print(s)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# c = [4.0, 8.5, 9.4]
# d = ['a', 'b', 'c']
# b = list(zip(a, c, d))
# print(b)

# dict_one = {'name': 'igor', 'Last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'Last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# two = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*two)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# s = ['red', 'blue', 'green']
# # j = 1
# for j, i in enumerate(s, 1):
#     print(j, ')', i, sep='')
#     # j += 1


# def funk(*args):
#     return args
#
#
# print(funk(5))
# print(funk(5, 2, 4))
# print((funk()))


# def summa(*param):
#     res = 0
#     for i in param:
#         res += i
#         return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))
# print(summa(3, 4, 5))
# # print(summa('a', 'b')
#
# print(sum((1, 2, 3, 4, 5, 6, 7, 8)))


# def ch(*args):
#     average = sum(args) / len(args)
#     print('Среднее арифметическое', average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num )
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 8, 7, 8, 9, 4, 5, 6, 1))


# def print_scores(student, *scores):
#     print('Student:', student, end=': ')
#     for score in scores:
#         print(score, end=' ')
#     print()
#
#
# print_scores('Jonathan', 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20)

# def func(**kwargs):
#     return kwargs
#
#
# print((func(a=1, b=2, c=3)))
# print(func())


# def info(**kwargs):
#     for k, v in kwargs.items():
#         print(k, 'is', v)
#     print()
#
#
# info(name='Irina', surname='Sharma', age=22, phone=123456789)
# info(name='Igor', surname='Wood', email='igor@gmail.com', countru='Russia', age=25, phone=65874615239)


# def func(a, n, m, *args, d=1, r=4, **kwargs):
#     return a, args, kwargs, d, n, m, r
#
#
# print(func(5, 1, 7, 9, 8, 6, b=2, c=3, d=7))


# name = 'Tom'  # глобальная
#
#
# def hi():
#     global name
#     name = 'Sam'
#     surname = 'Johnson'  # локальная
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# print(name)
# hi()
# bye()
# print(name)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 6
#
#
# def func(a):
#     # x = 2
#
#     def inner():
#         # x = 4
#         return a + x
#
#     return inner()
#
#
# print(func(3))


# import builtins
#
#
# names = dir(builtins)
#
#
# for t in names:
#     print(t)


# def outer(who):
#     who = 'Aleksey'
#
#     def inner():
#         print('Hello', who)
#
#     inner()
#
#
# outer('World!')


# def fun1():
#     a = 6  # 2
#
#     def fun2(b):
#         a = 4  # 5
#         print('Сумма:', a + b)  # 6
#
#     print('а =', a)  # 3
#     fun2(4)  # 4
#
#
# fun1()  # 1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('a =', a)
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Home_work


# def outer(a, b, c):
#
#     def inner(x, y):
#         return x * y
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# s = 0
#
#
# def outer(a, b, c):
#
#     def inner(x, y):
#         return x * y
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# def outer(a, b, c):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s = 2 * ((a * b) + (a * c) + (b * c))
#
#     inner()
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))
