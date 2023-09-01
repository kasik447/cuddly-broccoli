# import re
# s = "<p>Изображение <img alt='картинка' src=\"bg.jpg\"> - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+)(?P=q)>'  # (?P<name>...) (?P=name)
# print(re.findall(reg, s))


# s = 'Самолёт прилетает 10/23/2023. Будем рады вас видеть после 10/24/2023.'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))  # 23.10.2023


# s = 'yandex.com and yandex.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http:/\1", s))


# Файлы

# f = open('test.txt')
# f = open('C:\\Study\\python\\Test.txt')
# f = open('C:/Study/python/Test.txt')
# print(f)
# print(*f)


# f = open('test.txt', 'r')
# print(f.read(3))
# f.close()
#
# f = open('test.txt', 'r')
# print(f.read())
# f.close()


# f = open('text.txt', 'r')
# print(f.readline())  # '\n' new line
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open('text.txt', 'r')
# print(f.readlines(4))
# print(f.readlines())
# f.close()


# f = open('text.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# count = 0
# f = open('text.txt', 'r')
# for line in f:
#     count += 1
# f.close()
# print(count)


# f = open('text.txt', 'r')
# print(len(f.readlines()))
# f.close()


# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')
# f.close()


# f = open('xyz.txt', 'a')
# # print(f.write('\nNew text.'))
# f.close()


# f = open('xyz.txt', 'a')
# lines = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()


# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = 'Hello World!\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()


# f = open('test.txt')
# print(f.read(3))
# print(f.tell())  # На какой позиции находится визуальный курсор
# print(f.seek(1))  # Перемещает курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open('test4.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))  # 12
# print(f.tell())  # 15
# f.close()


# with open('test.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('test.txt', 'r+') as f:
#     print(f.read())


# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line[:6])


# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# get_line(lst)
# print('Done!')


# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)  # str
#
# nums_list = list(map(float, nums.split()))  # list(map(float, ['4.5', '2.8', '3.9', '1.0', '0.3', '4.33', '7.777'])
# # num_list = nums.split()
# print(nums_list)
# # print(type(nums_list[0]))
# print(len(nums_list))


# def longest_words(file):
#     with open('file2.txt', encoding='utf-8') as text:
#         w = text.read().split()
#         # print(w)
#         max_length = len(max(w, key=len))
#         # print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         # print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words('file2.txt'))


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
