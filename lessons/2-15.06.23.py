# У питона сильная типизация данных
# num1 = '2'
# num2 = 3
# print(type(num1))
# print(type(num2))
# res = int(num1) + num2
# res = num1 + str(num2)
# print(res)

# print(int(3.8945))
# print(float(3.8945))

# a = 3.8945
# a = round(a, 2)
# print(a)
# print(type(a))
#
# print(int(3.8945))
# print(round(3.8945))

# num1 = '5.2'
# num2 = 10
# print(type(num1))
# print(type(num2))
# res = float(num1) + num2  # 5.2 + 10
# print(res)

# name = 'Виктор'
# age = 28
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print()
# print('Меня зовут', name, '. Мне', age, 'лет.', sep='--', end='\n\n')
# print('Продолжение строки.')


# name = input('Введите имя: ')
# print('Hello, ', name, '!', sep='')

# num = int(input('Введите число: '))
# power = int(input('Введите степень: '))
# num = int(num)
# power = int(power)
# res = num ** power
# print(res)

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# num4 = int(input('Введите четвертое число: '))
#
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = sum1 / sum2
# print(round(res, 2))

# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)
#
# print(type(b1))

# False = '', 0, False, None

# print(bool('Python'))
# print(bool(''))  # False
# print(bool(12))
# print(bool(False))  # False
# print(bool(None))  # False


# a = None
# print(a)
# print(a is None)
# a = 5
# print(a)

# print(5 < 2)
# print('п' > 'П')

# print(2 < 4 < 9)  # True && True
# print(2 < 4 > 9)  # True && False
# print(2 * 5 > 7 >= 4 + 3)  # True && True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False


# && - and
# || - or
# ! - not

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 or 1 + 3 == 4)

# print(not 9 - 5)
# print(not 9 - 9)


# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)


# age = int(input('Введите свой возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешён')
# else:
#     print('Доступ запрещён')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# if b > a:
#     print('b > a')
# else:
#     print('a == b')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# if b > a:
#     print('b > a')
# if a == b:
#     print('a == b')


# a = 10
# b = 25
# if a > b:
#     print('a > b')
# elif b > a:
#     print('b > a')
# else:
#     print('a == b')


# a = (input('Введите первую сторону: '))
# b = (input('Введите вторую сторону: '))
# c = (input('Введите третью сторону: '))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Ваш треугольник равнобедренный')
# else:
#     print('Ваш треугольник разносторонний')


# day = int(input('Введите день недели цифрой: '))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('среда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     if day == 7:
#         print('воскресенье')
# else:
#     print('Такого дня недели не существует')

m = int(input('Введите номер месяца: '))
if m == 1 or m == 2 or m == 12:
    print('Зима')
elif 3 <= m <= 5:
    print('Весна')
elif 6 <= m <= 8:
    print('Лето')
elif 9 <= m <= 11:
    print('Осень')
else:
    print('Ошибка ввода')









