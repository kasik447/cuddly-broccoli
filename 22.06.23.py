# i = 1
# while i < 5:
#     print('Внешние циклы : i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 16:
#         if j % 2:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#    тело цикла

# for i in 'Hello!':
#     print(i)

# for color in 'red', 'blue', 'green':
#     print(color)

# for element in range(start, stop, step):
#     тело цикла

# for i in range(5, 100, 10):
#     print(i, end=' ')
#
# print()
#
# i = 5
# while i < 100:
#     print(i, end=' ')
#     i += 10

# a = int(input('Введите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('Done!')

# w = int(input('Введите ширину прямоугольника: '))
# h = int(input('Введите высоту прямоугольника: '))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# a = [latter for latter in 'Hello']
# print(a)

# num = [i for i in range(20) if i % 2 == 0]
# print(num)

#  Список (list)
# nums = [8, 3, 4, 1, 9, 'Hello', 2.5]
#      [0, 1, 2, 3, 4,    5,     6]
#      [-7,-6,-5,-4,-3,  -2,    -1]
# print(nums)
# print(type(nums))
# print(nums[-1])
# print(nums[3])
# nums[3] = 256
# nums[0] += 100
# print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# b = list('Hello')
# print(b)
# print(type(b))

# n = list(range(2, 10, 3))
# print(n)

# a = [0 for i in range(5)]
# print(a)

# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)

# a = [i * 3 for i in 'List']
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)


# a = [0] * int(input('Кол-во элементов в списке: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)


# a = [int(input('-> ')) for i in range(int(input('n: ')))]
# print(a)

# a = ['один', 'два', 'три', 'четыре', 'пять']
#
# for i in range(len(a)):
#     print(a[i], end=' ')
# print()
# for el in a:  # один два три четыре пять
#     print(el, end=' ')

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print('Сумма отрицательных элементов:', s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print('Кол-во четных элементов:', k)
# print('Сумма нечетных элементов:', s)

a = [int(input('-> ')) for i in range(int(input('n = ')))]
print(a)
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i], end=' ')






























