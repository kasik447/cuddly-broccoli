# Множественное наследование

# class Creature:
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def __init__(self, name):
#         Creature.__init__(self, name)
#         print('Инициализатор класса Animal')
#
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def __init__(self, age):
#         self.age = age
#         print('Инициализатор класса Pet')
#
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# dog = Dog('Buddy')
# dog.bark()
# # dog.play()
# # dog.sleep()
# # print(Dog.__mro__)


# class A:
#     def __init__(self):
#         print('Инициализатор класса А')
#
#
# class AA:
#     def __init__(self):
#         print('Инициализатор класса АА')
#
#
# class B(A):
#     def __init__(self):
#         print('Инициализатор класса B')
#
#
# class C(AA):
#     def __init__(self):
#         print('Инициализатор класса C')
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print('Инициализатор класса D')
#
#
# d = D()
# # print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Styles:
#     def __init__(self, color, width):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         print('Инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100))
# l1.draw()


# Миксины (примеси)


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# subclass = MySubClass()
# subclass.display('Строка будет печататься и сохраняться в файл')


# class Goods:
#     def __init__(self, name, weight, price):
#         print('Init Goods')
#         super().__init__()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init MixinLog')
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()


# Перегрузка операторов

# 24*60*60 86400 (кол-во секунд в одном дне)


# class CLock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть числом')
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{CLock.__get_form(h)}:{CLock.__get_form(m)}:{CLock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, CLock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return CLock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, CLock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = CLock(100)
# c2 = CLock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# if c1 != c2:
#     print('Время разное')
# else:
#     print('Время одинаковое')
# # c4 = CLock(300)
# # c3 = c1 + c2 + c4
# # c4 += c1 + c2
# # print(c4.get_format_time())
# # print(c3.get_format_time())


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

    def __sub__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return CLock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return CLock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return CLock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return CLock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.sec == other.sec

    def __gt__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.sec >= other.sec

    def __lt__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, CLock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return self.sec <= other.sec


c1 = CLock(600)
c2 = CLock(200)
print(f'c1: {c1.get_format_time()}')
c3 = c1 - c2
print(f'c1 - c2: {c3.get_format_time()}')
c3 = c1 * c2
print(f'c1 * c2: {c3.get_format_time()}')
c3 = c1 // c2
print(f'c1 // c2: {c3.get_format_time()}')
c3 = c1 % c2
print(f'c1 % c2: {c3.get_format_time()}')
c1 -= c2
print(f'c1 -= c2: {c1.get_format_time()}')
c1 *= c2
print(f'c1 *= c2: {c1.get_format_time()}')
c1 //= c2
print(f'c1 //= c2: {c1.get_format_time()}')
c1 %= c2
print(f'c1 %= c2: {c1.get_format_time()}')

print()

c3 = c1 + c2
print(f'c3 > c1: {c3 > c1}')
print(f'c3 => c1: {c3 >= c1}')
print(f'c3 < c1: {c3 < c1}')
print(f'c3 <= c1: {c3 <= c1}')
