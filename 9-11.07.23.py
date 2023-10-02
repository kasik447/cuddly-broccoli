# [1, 2, 3, 4, 5]
# s = frozenset({i ** 2 for i in range(10)})
# print(s)

# Словари (dict)

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 3: 0}
# print(type(d))
# print(lst[0])
# print(d['one'])
# print(lst[2])
# print(d[3])

# d = {'one': 1, 'two': 2, 3: 0}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# users = [('a', 'b'), ['c', 'd'], ['e', 'f']]
# print(users)
# d_users = dict(users)
# print(d_users)
# lst = list(d_users)
# print(lst)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[4])
# d[4] = 20 * 2
# print(d)

# s = {0, 1, 2, 0}
# print(s)
# s.remove(3)
# print(s)
# d = {0: 'text', 'one': 1, (1, 2.3): 'кортеж', 'список': [5, 7, 8, 9], True: 1}
# print(d)
# print(d[(1, 2.3)])
# print(d['список'][1])
# print('one' in d)
# del d[0]
# print(d)
# print(d['one1'])
# lst = [1, 2, 3]
# print(lst[3])

# d = {'one': 1, 'two': 2, 'three': 3}
#
# # for key in d:
# #     print(key, d[key])
# # key = 'two'
# # if key in d:
# #     del d[key]
#
# key = 'four'
#
# try:
#     del d[key]
# except KeyError:
#     print('Элемента с ключом ' + key + ' нет в словаре')
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# res = 1
# for key in d:
#     res *= d[key]
# print(res)


# d = dict()  # {}
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# dislike = int(input('Какой элемент исключить: '))
# del d[dislike]
# print(d)


# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# print(len(d))
# print(sum(d))

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 9, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium 63220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         k = int(input('Количество: '))
#         goods[n][1] = k
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')


# d = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(d)
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())  # список ключей и значений
# # for i, j in d.items():
# #     print(i, j)
#
# print(set(d.values()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
#
# print('D =', d)
# print('D2 =', d2)
#
# d2['b'] = 5
# d['e'] = 7
#
# print('D =', d)
# print('D2 =', d2)


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.update({'a': 7, 't': 9})  # обновление словаря
# d.update([('b', 5), ('q', 7)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)


# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# # d.clear()  # очистили словарь
# # item = d.pop('b')  # удаляет ключ и значение по ключу, но возвращает значение
# item = d.popitem()  # удаляет ключ и значение последние в словаре, и возвращает кортеж из удаляемых элементов
# print(item)
# print(d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # new_d = dict()
#
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
#
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')


#  Home_work

region = {
    'John': {
        'N': 3056,
        'S': 8463,
        'E': 8441,
        'W': 2694
    },
    'Tom': {
        'N': 4832,
        'S': 6786,
        'E': 4737,
        'W': 3612
    },
    'Anne': {
        'N': 5239,
        'S': 4802,
        'E': 5220,
        'W': 1859
    },
    'Fiona': {
        'N': 3056,
        'S': 3645,
        'E': 8821,
        'W': 2451
    }
}

for x in region:
    print(x)
    for y in region[x]:
        print(y, ':', region[x][y])

name = input('Имя: ')
r = input('Регион: ')
print(region[name][r])
new = int(input('Новое значение: '))
region[name][r] = new
print(region[name])
