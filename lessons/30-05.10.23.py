# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += str(i) + ', '
#         # return f'Студент: {self.name} - {a[:-2]}'
#
#         # a = ', '.join(map(str, self.marks))
#         # return f'Студент: {self.name} - {a}'
#
#         return f'Студент: {self.name} - {", ".join(map(str, self.marks))}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_marks):
#         self.marks[index] = new_marks
#
#     def average_marks(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, filename):
#         data = {'name': self.name, 'marks': self.marks}
#         with open(filename, 'w') as f:
#             json.dump(data, f)
#
#     def load_from_file(self, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         # a = ''
#         # for i in self.students:
#         #     a += str(i) + '\n'
#         # return f'{a}'
#
#         a = "\n".join(map(str, self.students))
#         return f'Группа: {self.group}\n{a}'
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def dump_group(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_group(file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # file1 = 'student.json'
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(1, 5)
# # print(st1)
# # print(st1.average_marks())
# # st1.dump_to_json(file1)
# # st1.load_from_file(file1)
#
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# my_group.add_student(st3)
# # print(my_group)
# # print()
# my_group.remove_student(1)
# print(my_group)
#
# print()
#
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# print(my_group2)
#
# Group.change_group(my_group, my_group2, 0)
# print('-' * 40)
# print()
# print(my_group)
# print()
# print(my_group2)
#
# file2 = 'group.json'
# # Group.dump_group(file2, my_group)
# # Group.dump_group(file2, my_group2)
# Group.upload_group(file2)


# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# # users = ['9']
# max_user = ' and '.join(users)
# print(max_user)
#
# m = 's' if len(users) > 1 else ''
# print(f'User{m} {max_user} completed {max_complete} TODOs')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('data.json', 'w') as f:
#     filter_todos = (list(filter(keep, todos)))
#     json.dump(filter_todos, f, indent=2)


# CSV (Comma Separated Values) - переменные, разделенные запятыми

import csv

with open('data.csv') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            print(f'\t{row[0]} - {row[1]}. Родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк')



