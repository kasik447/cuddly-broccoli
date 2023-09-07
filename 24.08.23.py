# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
# with open('one.txt', 'w') as f:
#     f.write(text)

#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)


# read_file = 'one.txt'
# write_file = 'two.txt'
# res = 'three.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'r', encoding='utf-8') as fw, open(res, 'w') as res:
#     # f1 = fr.readlines()
#     # f2 = fw.readlines()
#     # print(f1)
#     # print(f2)
#     # f3 = f1 + f2
#     # res.writelines(f3)
#
#     for i, j in zip(fr, fw):
#         print(i)
#         print(j)
#         res.write(i[:-1] + ' = > ' + j)


#  Модуль OS (OS.PATH)

import os
# import os.path

# print('Текущая директория:', os.getcwd())  # Путь к файлу
# print(os.listdir())  # Список папок и файлов, находящиеся в текущей директории
# print(os.listdir('..'))


# os.mkdir('nested1')  # Создать папку, но только одну, без промежуточных путей
# os.makedirs('nested1/nested2/nested3')  # Может создавать вложенные папки

# os.remove('test.txt')  # Удаляет файл

# os.remove('folder/file.txt')

# os.rmdir('folder1')  # Удаляет папку (но только пустую)

# os.rename('xyz.txt', 'first.txt')  # переименование и перемещение файла
# os.rename('first.txt', 'nested1/first.txt')  # переименование и перемещение файла
# os.rename('folder', 'nested1/folder')


# for root, dirs, files in os.walk('nested1', topdown=False):
#     print('Root:', root)
#     print('Dirs:', dirs)
#     print('Files:', files)


# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в папке {root_tree}')
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#
#     print('-' * 50)
#
#
# remove_empty_dirs('nested1')


import os.path

# print(os.path.split(r'C:\Study\python\nested1\nested2\nested3\two.txt'))  # Разбивает путь на кортежи(путь, имя док-а)
#
# print(os.path.exists(r'C:\Study\python\nested1\nested2\nested3\two.txt'))  # проверяет существование заданного пути
#
# print(os.path.join(r'C:\Study', 'nested1', 'nested2', 'two.txt'))


# dirs = [r'Work\F1', r'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         print(file_path)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f11.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f'Какой-то текст для файла {file}')
#
#
# def print_three(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, file in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(file)
#     print('-' * 50)
#
#
# print_three('Work', topdown=False)
# print_three('Work', topdown=True)


import time


# path = '27.06.23.py'
# size = os.path.getsize(path)
# # print(os.path.getsize(path), 'bytes')
# print(size // 1024, 'KB')
# ctime = os.path.getctime(path)
# # print(os.path.getctime(path))  # Время создания файла в секундах
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(ctime)))  # Время создания файла в секундах
# print(os.path.getatime(path))  # Время последнего доступа к файлу в секундах
# print(os.path.getmtime(path))  # Время последнего изменения файла в секундах


# file_path = 'nested1/nested2/text2.txt'

# if os.path.exists(file_path):
#     dir0, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f'{name} ({dir0}) - Время последнего доступа к файлу:', atime, 'сек.')
# else:
#     print(f'Файл {file_path} не существует!')


# file_path = 'nested1/nested2/text2.txt'
#
# print(os.path.isfile(file_path))  # Возвращает TRUE, если путь является файлом
# print(os.path.isdir(file_path))  # Возвращает TRUE, если путь является папкой


# dir_name = 'nested1'
#
# objs = os.listdir(dir_name)
# print(objs)
#
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     else:
#         print(f'{obj} - dir')


# Homework

dir_name = 'nested1'

objs = os.listdir(dir_name)
print(objs)
res1 = []
res2 = []

for obj in objs:
    j = os.path.join(dir_name, obj)
    if os.path.isfile(j):
        res1.append(j)
    else:
        res2.append(j)

# print(res1)
# print(res2)
print(res1 + res2)








