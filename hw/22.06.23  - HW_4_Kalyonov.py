n = [int(input('-> ')) for i in range(int(input('n = ')))]
s = k = m = 0
for i in range(len(n)):
    if n[i] > 0:
        k += 1
        s += n[i]
m = s / k
print('Среднее арифметическое:', round(m, 2))


