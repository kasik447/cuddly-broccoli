# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым неотрицательным числом')
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  #
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# print(s1.__dict__)
# # s1.marks[2] = 4
# s1[10] = 4
#
# del s1[2]
# print(s1.__dict__)
#
# # l1 = [5, 5, 3, 4, 5]
# # l1.extend([None] * 6)
# # print(l1)


class CLock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError('Секунды должны быть числом')
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{CLock.__get_form(h)}:{CLock.__get_form(m)}:{CLock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __add__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return CLock(self.sec + other.sec)

    def __eq__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть строкой')

        if item == 'hour':
            return (self.sec // 3600) % 24
        elif item == 'min':
            return (self.sec // 60) % 60
        elif item == 'sec':
            return self.sec % 60

        return 'Неверный ключ'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')

        if not isinstance(value, int):
            raise ValueError('Значение должно быть целым числом')

        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24

        if key == 'hour':
            self.sec = s + 60 * m + value * 3600
        elif key == 'min':
            self.sec = s + 60 * value + h * 3600
        elif key == 'sec':
            self.sec = value + 60 * m + h * 3600


c1 = CLock(80000)
print(c1['hour'], c1['min'], c1['sec'])
c1['hour'] = 14
c1['min'] = 18
c1['sec'] = 55
# c2 = CLock(200)
print(c1.get_format_time())
# print(c2.get_format_time())
# if c1 != c2:
#     print('Время разное')
# else:
#     print('Время одинаковое')
# c4 = CLock(300)
# c3 = c1 + c2 + c4
# c4 += c1 + c2
# print(c4.get_format_time())
# print(c3.get_format_time())


# from random import randint, choice
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == 'M':
#             return f'{self.name} is good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is good girl!!!'
#         else:
#             return f'{self.name} is good Kitty!!!'
#
#     def __repr__(self):
#         return f'Cat(name="{self.name}", age={self.age}, pol={self.pol})'
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat('Not name', 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError('Types are not supported!')
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Elsa', 5, 'F')
# # cat3 = Cat('Murzik', 3, 'M')
# print(cat1)
# print(cat2)
# print(cat1 + cat2)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('Python')
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}.')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает')
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}.')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает')
#
#
# cat = Cat('Пушок', 2.5)
# dog = Dog('Мухтар', 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.surname} {self.name} {self.age}', end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.group} {self.rating}', end=' ')
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, experience):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.experience}', end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#         super().__init__(surname, name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f'{self.topic}', end=' ')
#
#
# groups = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "Python_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in groups:
#     i.info()
