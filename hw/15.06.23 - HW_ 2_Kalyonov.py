num = int(input('Введите пятизначное число: '))
user_number = num

n5 = num % 10
num = num // 10
n4 = num % 10
num = num // 10
n3 = num % 10
num = num // 10
n2 = num % 10
num = num // 10
n1 = num % 10

prod = n5 + n4 + n3 + n2 + n1
print('Произведение цифр числа ', user_number, ': ', prod, sep='')

middle = (n5 + n4 + n3 + n2 + n1) / 5
middle = round(middle, 1)
print('Среднее арифметическое:', middle)


