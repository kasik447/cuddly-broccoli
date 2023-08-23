# HomeWork

n = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
print(n)

for i in set(n):
    print('Количество', i, '=', n.count(i))
