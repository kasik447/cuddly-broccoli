# Удаляют пробельные символы в строке
# print('   py'.lstrip())
# print('py   '.rstrip())
# print('   py   '.strip())

# print('https://www.python.org'.lstrip('/:pths'))
# print('https://www.python.org'.lstrip('/:pths').rstrip('org.'))
# print('https://www.python.org'.strip('/:pthsorg.'))


# s = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# print(s.replace('Nython', 'Python', 2))  # Поиск и замена


# Преобразует итерируемый объект в строку
# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print('...'.join(['1', '99']))
# print(':'.join('Hello'))


# print('Строка разделенная пробелами'.split())  # Разбивает строку на список подстрок
# print('www.python.org.ru'.split('.', 1))
# print('www.python.org.ru'.rsplit('.', 1))

# a = input('-> ').split()
# print(a)


# a = input('Введите ФИО полностью через пробел: ').split()
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')


# Регулярные выражения

import re
# from re import split

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'я'
# print(re.findall(reg, s))  # Возвращает список, содержащий все совпадения или []
# print(re.search(reg, s))  # Возвращает первое совпадение с искомым шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))  # Возвращает первое совпадение с искомым шаблоном, только в начале строки
#
# print(re.split(reg, s, 5))  # Разбивает строку на список подстрок по заданному шаблону
#
# print(re.sub(reg, '!', s))  # Поиск и замена

#
# s = 'Я ищу совпадения в 2023 году. [^] И я их найду в 2 счёта. 47896. Hello World'
# reg = r'[2023]'
# # reg = r'[12][0-9][0-9][0-9]'
# # reg = r'[А-ЯЁа-яё]'
# # reg = r'[А-яЁё]'
# # reg = r'[A-Za-z]'
# # reg = r'[A-z]'
# # reg = r'[\[^\]]'
# reg = r'[^0-9]'
# print(re.findall(reg, s))
# print(ord('А'))
# print(ord('Я'))
# print(ord('а'))


# s = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Е01:09'
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))


s = 'Я ищу совпадения в 2023 году. [^] И я их найду в 2 счёта. 478_9-6. Hello World 2000000000000'
# reg = r'\d'  # [3-5] [\d] - Поиск одной любой цифры
# reg = r'\w'  # Буквы, цифры и символ подчёркивания(_)
# reg = r'\s'  # Пробельные символы, табуляции и перенос на другую строчку
# reg = r'\S'  # Противоположные действия(не пробелы, не табуляции и не переносы)
# reg = r'\W'  # Противоположные действия
# reg = r'\D'  # Противоположные действия
reg = r'20*'
print(re.findall(reg, s))

# + - от 1 до бесконечности повторений
# * - от 0 до бесконечности повторений
# ? - от 0 до 1 повторения


d = 'Цифры: 7, +17, -42, 0013, 0.3'
# print(re.findall(r'[+-]?\d+\.?\d*', d))
print(re.findall(r'[+-]?[\d.]+', d))


