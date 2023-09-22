# class Point:
#     __slots__ = ['__x', '__y', 'z']
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_x('100')
# p1.z = 5
# # print(p1.__dict__)
# print(p1.z)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
#
#     def __get_x(self):
#         return self.__x
#
#     def __del_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = '100'
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property   # получение данных
#     def x(self):
#         return self.__x
#
#     @x.setter   # установка данных
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
#
#     @x.deleter   # Удаление данных
#     def x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = '100'
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, o):
#         self.__old = o
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person('Irina', 26)
# print(p1.__dict__)
# p1.name = 'Igor'
# p1.old = 30
# print(p1.name)
# # del p1.name
# # del p1.old
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# # print(Point.__dict__)
# print(p1.get_count())
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# class Numbers:
#     # @staticmethod
#     # def max(a, b, c, d):
#     #     mx = a
#     #     if b > mx:
#     #         mx = b
#     #     if c > mx:
#     #         mx = c
#     #     if d > mx:
#     #         mx = d
#     #     return mx
#
#     @staticmethod
#     def max(*args):
#         res = args[0]
#         for i in args:
#             if i > res:
#                 res = i
#         return res
#
#     @staticmethod
#     def min(*args):
#         res = args[0]
#         for i in args:
#             if i < res:
#                 res = i
#         return res
#
#     # @staticmethod
#     # def average(*args):
#     #     return sum(args) / len(args)
#
#     # @staticmethod
#     # def average(*args):
#     #     res = 0
#     #     count = 0
#     #     for i in args:
#     #         res += i
#     #         count += 1
#     #     return res / count
#
#     @staticmethod
#     def average(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print('Максимальное число:', Numbers.max(3, 5, 7, 9))
# print('Минимальное число:', Numbers.min(3, 5, 7, 9))
# print('Среднее арифметическое:', Numbers.average(3, 5, 7, 9))
# print('Факториал числа:', Numbers.factorial(5))
# # 5! = 1*2*3*4*5


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.day}-{self.month}-{self.year}'
#
#
# # dt1 = Date.from_string('23.10.2023')
# # print(dt1.string_to_db())
# # dt2 = Date.from_string('21.12.2022')
# # print(dt2.string_to_db())
#
# dates = [
#     '30.12.2023',
#     '20-12-2023',
#     '01.01.2023',
#     '12.31.2023'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         dt1 = Date.from_string(string_date)
#         print(dt1.string_to_db())
#     else:
#         print('Неправильная дата или формат строки с датой!')


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт')
        print('*' * 50)

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):
        print('Информация о счёте:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)


acc = Account('Долгих', '12345', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()

