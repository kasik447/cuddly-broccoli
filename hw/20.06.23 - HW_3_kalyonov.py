k = int(input('Введите число от 1 до 99: '))
if 1 <= k <= 99:
    if k % 10 == 1:
        print(k, 'копейка')
    elif 11 <= k <= 14:
        print(k, 'копеек')
    elif k % 10 == 2 or k % 10 == 3 or k % 10 == 4:
        print(k, 'копейки')
    else:
        print(k, 'копеек')
else:
    print('Ошибка ввода данных')
