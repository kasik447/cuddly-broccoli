# import time
# import asyncio
#
#
# async def fun1(x):
#     print(x ** 2)
#     await asyncio.sleep(3)
#     print('fun1 завершена')
#
#
# async def fun2(x):
#     print(x ** 0.5)
#     await asyncio.sleep(3)
#     print('fun2 завершена')
#
#
# async def main():
#     task1 = asyncio.create_task(fun1(4))
#     task2 = asyncio.create_task(fun2(4))
#
#     await task1
#     await task2
#
#
# print(time.strftime('%X'))
# asyncio.run(main())
# print(time.strftime('%X'))

# Напишите, пожалуйста, программу (функцию или метод),
# которая будет печатать числа от 0 до 1000,
# кратные трём и не кратные пяти, сумма цифр в которых меньше десяти.


# def print_numbers():
#     for i in range(1, 1000):
#         if i % 3 == 0 and i % 5 != 0:
#             sm = 0
#             n = i
#             while n > 0:
#                 sm += n % 10
#                 n //= 10
#             if sm < 10:
#                 print(i)
#
#
# print_numbers()

# def print_numbers():
#     for number in range(1, 1000):
#         if number % 3 == 0 and number % 5 != 0:
#             digits = [int(digit) for digit in str(number)]
#             if sum(digits) < 10:
#                 print(number)
#
# print(print_numbers())


# На диске лежит очень большой файл объёмом более 100 Gb.
# Файл содержит целые числа — по одному в каждой строке.
# Нужно отсортировать их по возрастанию.
# Опишите алгоритм решения такой задачи


# Вариант 2
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([3, 20, 5, 1, 10]))


# Вариант 1
def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    new_arr = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_arr.append(array.pop(smallest))
    return new_arr


print(selection_sort([5, 2, 33, 7, 10]))


