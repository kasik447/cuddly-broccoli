# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = tuple((2, 5, 7, 9, 8))
# print(a)
# print(a[-1])
# print(a[1:3])

# s = tuple(input('=> ') for i in range(5))
# print(s)

# from random import randint
#
# s = tuple(randint(0, 10) for i in range(5))
# print(s)


# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(t3.count('a'))
# ch = 'w'
# if ch in t3:
#     print(t3.index(ch))
# else:
#     print('Такого символа нет')

# for i in t3:
#     print(i * 2, end=' ')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl_1 = ran(0, 5)
# tpl_2 = ran(-5, 0)
# print(tpl_1)
# print(tpl_2)
# tpl_3 = tpl_1 + tpl_2
# print(tpl_3)
# print('0 =>', tpl_3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# del t[4][0]
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # n, year, married = user
# n, year, married = get_user()
# print(n, year, married)


# tpl = (10, 20, 30)
# del tpl


# tpl = (10, 20, 30)
# lst = list(tpl)
# lst.append(50)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.718))),
# )
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана: ', country_name, '. Население: ', country_population, sep='')
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород: ', city_name, '. Население: ', city_population, sep='')


# Множество (set)
# s = {'banana', 'apple', 'orange', 'banana', 'apple'}
# print(s)
# print(type(s))
# for i in s:
#     print(i)


# a = set()
# print(a)
# print(type(a))

# s = {i * i for i in range(10)}
# print(s)
# print(64 not in s)

#
# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in s if 'a' not in i}
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s]
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# print(a)
#
# for i in s:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# a = {'Tom', 'Bob', 'Alice'}
# a.add('Sam')
# print(a)
# # a.remove('Tom')
# # a.add('Ann')  # KeyError
# # print(a.pop())
# # a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # print(c)
# # c = a - b
# # print(c)
# c = a ^ b
# print(c)
# # a |= b
# # print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))



# HomeWork

n = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
print(n)

for i in set(n):
    print('Количество', i, '=', n.count(i))



