# import pickle


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
#
# print(item3.__dict__)
# print(item3)


# import json

#
# data = {
#     'name': 'Olga',
#     'age': 25,
#     20: None,
#     'hobbies': ('running', 'singing'),
#     True: 1,
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         }
#     ],
# }
#
# print(data, end='\n\n')
#
#
# # with open('data_file.json', 'w') as fw:
# #     json.dump(data, fw, indent=4)
# #
# #
# # with open('data_file.json', 'r') as fw:
# #     file = json.load(fw)
# #
# # print(file)
#
#
# json_str = json.dumps(data)
# print(json_str, type(json_str))
# st = json.loads(json_str)
# print(st, type(st))


# x = {
#     'name': 'Виктор'
# }
# y = json.dumps(x)
# print(json.dumps(x, ensure_ascii=False))
# # print(json.loads(y))


import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())


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
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(1, 5)
# # print(st1)
# # print(st1.average_marks())
#
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts = [st1,  st2]
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
