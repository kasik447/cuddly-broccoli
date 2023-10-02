# Замыкания


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# i = outer(5)
# print(i(10))
#
# j = outer(6)
# print(j(20))

# print(outer(4)(6))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res1()


# students = {
#     'Alica': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make(lower, upper):
#     def inner(exam):
#         return {k: v for k, v, in exam.items() if lower <= v < upper}
#
#     return inner
#
#
# bal_A = make(80, 100)
# bal_B = make(70, 80)
# bal_C = make(50, 70)
# bal_D = make(0, 50)
# print(bal_A(students))
# print(bal_B(students))
# print(bal_C(students))
# print(bal_D(students))


# def func(a, b):
#
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())  # сумма
# print(obj1.sub())  # разность
# print(obj1.mul())  # произведение


# Анонимные функции (lambda-выражения)


# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 2, 5, 4, 6, 7, 4, 5, 2))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(42)
# print(f(1))
#
#
# outer2 = lambda n: lambda x: x + n
#
#
# f2 = outer2(42)
# print(f(1))
#
# print((lambda n: lambda x: x + n)(42)(1))
#
#
# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))


# def sort_val(i):
#     return i[1]
#
#
# d = {'c': 10, 'a': 15, 'b': 4}
# q = list(d.items())
# print(q)
# # q.sort(key=lambda i: i[1], reverse=True)
# q.sort(key=sort_val, reverse=True)
# print(q)
# d1 = dict(q)
# print(d1)


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)


# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](12, 5)
# print(b)


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[2]()


# map(func, iter), filter(func, iter)

# def mult(t):
#     return t * 2


# lst = [2, 8, 12, 5, 10]

# a = list(map(mult, lst))
# a = list(map(lambda t: t * 2, lst))
# a = set(map(lambda t: t * 2, [2, 8, 12, 5, 10]))
# print(a)


# t = (2.88, -1.75, 100.5)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
# t3 = tuple(map(int, t))
# print(t3)


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# filter(func, iter)

# t = ('abcd', 'ebc', 'cdert', 'def', 'gfi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# Home_work
# 1
# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# res1 = sorted(students, key=lambda item: item['name'], )
# print(res1)
# res2 = sorted(students, key=lambda item: item['final'], reverse=True)
# print(res2)

# 2
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
#
# res1 = list(map(lambda x: x ** 2, nums))
# print(res1)
#
# res2 = list(map(lambda x: x ** 3, nums))
# print(res2)
