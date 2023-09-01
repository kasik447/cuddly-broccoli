# Homework

f = open('home_text.txt', 'w')
f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
f.close()

f = open('home_text.txt', 'r')
read_text = f.readlines()
print(read_text)
f.close()

delete = int(input('pos = '))
res = read_text.pop(delete)
print(read_text)

f = open('home_text.txt', 'w')
f.writelines(read_text)
f.close()
