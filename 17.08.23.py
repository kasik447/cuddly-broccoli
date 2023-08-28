import re
#
# d = 'Цифры: 7б +17б -42б 0013б 0.3'
# print(re.findall(r'[+=]?[\d.]+', d))

# s = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub('#.*', '', s))
# # Дата рождения: 05.03.1987
# print('Дата рождения:', re.sub('-', '.', re.sub('#.*', '', s)))


# s = '12 сентября 2023 год 4684534'
# reg = r'\d{,4}'  # одна любая цифра 4 раза подряд
# print(re.findall(reg, s))


# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'^\w+\s\w+'
# # reg = r'\w+\.$'
# print(re.findall(reg, s))


# def validate_login(name):
#     return re.findall(r'^[A-Za-z_-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Pytsdfs'))


# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))


# text = 'Hello world'
# print(re.findall(r'\w\+', text, flags=re.DEBUG))


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))


# text = '''
# one
# two
# '''
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, flags=re.DOTALL))
#
# print(re.findall('one$', text))
# print(re.findall('one$', text, flags=re.MULTILINE))


# print(re.findall('''[a-z.-]+ @[a-z.-]+''', 'test@mail.ru'))
# print(re.findall('''
# [a-z.-]+   # part 1
# @          # @
# [a-z.-]+   # part 2
# ''', 'test@mail.ru', flags=re.VERBOSE))


# text = '''Python,
# python,
# PYTHON
# '''
# reg = '(?im)^python'
# print(re.findall(reg, text))


# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*?>', text))
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# s = '12 сентября 2023 год 4684534'
# reg = r'\d{2,4}?'  # одна любая цифра 4 раза подряд
# print(re.findall(reg, s))


# s = "<p>Изображение <img  alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))


# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Ольга|Виталий|Николай'
# print(re.findall(reg, s))


# s = 'int = 4, float = 4.0, double = 8.0f'
# # reg = r'(?:int|double)\s*=\s*\d+[.\w+]*'
# reg = r'(int|double)\s*=\s*(\d+[.\w+]*)'
# print(re.findall(reg, s))

#
# # s = '127.0.0.1'
# s = '192.168.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))


# s = 'Word2016, PS6, AI5'
# reg = r'(([a-z])+(\d+))'
# print(re.findall(reg, s, re.I))


# s = '5 + 7*2 - 4'
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, s))
#
#
# s1 = '5 + 7*2 - 4'
# reg1 = r'\s*([+*-])\s*'
# print(re.split(reg1, s1))

# 1000 - 2099
# a = '12-08-2021'
# reg = r'(0[0-9]|[1-2][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(reg, a))


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'(\d+)\s(\D+)'
# print(re.search(reg, s).group(0))
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])


# text = '''
# Самара
# Москва
# Тверь
# Уфа
# Казань
# '''
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f'<option value={count}>{m.group(1)}</option>\n'
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# Homework

s = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3-67@i.ru, 1login@ru.name.ru'

reg = r'[\d*\w*@._-]+@[\d*\w*@._-]+\.[\d*\w*@.]+'
# reg = r'[a-zа-я0-9_.+-]+@[a-z0-9]+\.[a-z0-9-.]+'

print(re.findall(reg, s))





