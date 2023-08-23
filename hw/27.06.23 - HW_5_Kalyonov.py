# HomeWork
p = []
a = [0] * int(input('Введите длину списка: '))

for i in range(len(a)):
    a[i] = int(input('Введите элемент списка: '))
    if a[i] >= 0:
        p.append(a[i])
print('Список:', a)
print('Новый список, состоящий из положительный элементов:', p)

max1 = p[0]
for j in p:
    if j > max1:
        max1 = j
print('Наибольший элемент списка:', max1)
