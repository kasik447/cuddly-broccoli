
# class Person:
#     skill = 10
#     name = ''
#     surname = ''
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print('Данные сотрудника:', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника:', self.skill)
#
#
# p1 = Person()
# p1.print_info('Виктор', 'Резник')
# p1.add_skill(3)
# print()
# p2 = Person()
# p2.print_info('Анна', 'Долгих')
# p2.add_skill(2)


# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):  # Инициализатор - присвоение первоначального значения
#         self.name = name
#         self.surname = surname
#         print('Инициализатор')
#
#     def __del__(self):  # Деструктор
#         print('Деструктор')
#
#     def print_info(self):
#         print('Данные сотрудника:', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника:', self.skill)
#
#
# p1 = Person('Виктор', 'Резник')
# p1.print_info()
# p1.add_skill(3)
# # del p1
# p1 = 5
# print()
# p2 = Person('Анна', 'Долгих')
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p2 = Point(2, 7)
# print(p2.get_coord())
# p3 = Point(10, 20)
# print(p3.get_coord())
# print(Point.count)
# print(p3.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним.")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("R-5ST")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1, droid2, droid3
# print("Численность роботов:", Robot.k)


class Point:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        self.__x = x
        self.__y = y

    @staticmethod
    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coord(self, x, y):  # установить
        # if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y,float):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def get_coord(self):  # получить
        return self.__x, self.__y

    def set_x(self, x):
        if Point.__check_value(x):
            self.__x = x
        else:
            print("Координата X должна быть числом")

    def get_x(self):
        return self.__x


p1 = Point(5, 10)
# print(p1.__x, p1.__y)
# p1.__x = 100
# p1.__y = 'abc'
# print(p1.__x, p1.__y)

# p1.set_coord(20.5, 50)
print(p1.get_coord())
p1.set_x('100')
print(p1.__dict__)
# print(Point.__dict__)
# print(p1._Point__x)
p1._Point__x = 111
print(p1.__dict__)
