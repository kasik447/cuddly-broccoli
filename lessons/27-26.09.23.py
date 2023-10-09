# Функторы - объекты класса, которые можно выполнять как функции

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip('?:!.; ')
# print(s1('  ?   Hello World!    ; '))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой')
#
#         return args[0].strip(self.__chars)
#
#
# s2 = StringStrip('?:!.; ')
# print(s2('  ?   Hello World!    ; '))


# Класс как декоратор


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.fn()
#         print('После вызова функции')
#
#
# @MyDecorator
# def func():
#     print('Hello')
#
#
# func()


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         return f'Перед вызовом функции\n{self.fn(x, y)}\nПосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         return self.fn(x, y) ** 2
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 3))


# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         print('*' * 50)
#         # print('args', args)
#         # print('kwargs', kwargs)
#         return f'Перед вызовом функции\n{self.fn(*args, **kwargs)}\nПосле вызова функции'
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b, c):
#     return a * b * c
#
#
# @MyDecorator
# def func3(a, b):
#     return a + b
#
#
# print(func(2, 5))
# print(func2(2, 5, 2))
# print(func3(b='World', a='Hello '))


class Decor:
    def __init__(self, string):
        self.string = string

    def __call__(self, func):
        def wrap(x, y):
            print('*' * 20)
            print(self.string, end=' ')
            func(x, y)
            print('=' * 20)

        return wrap


@Decor('Значения:')
def add(a, b):
    print(a, b)


add(2, 5)


# Декорирование методов


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Виталий', 'Карасев')
# p1.info()


# Декораторы класса


# def decor(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decor
# class ActualClass:
#     def __init__(self):
#         print('Инициализатор')
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# Дескрипторы (класс, у которого будут определены магические методы: гет, сет, делит)
# - это класс (название может быть любым), в котором могут быть определены следующие методы:
# __get__()
# __set__()
# __delete()
# __set_name__()

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{value} должно быть строкой')
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)

# @property
# def name(self):
#     return self.__name
#
# @name.setter
# def name(self, value):
#     self.__name = value
#
# @property
# def surname(self):
#     return self.__surname
#
# @surname.setter
# def surname(self, value):
#     self.__surname = value


# p = Person('Ivan', 'Petrov')
# p.name.set('Igor')
# print(p.name.get())
# DRY (Don't Repeat Yourself) - не повторяйся


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', 'Petrov')
# p.name = 'Igor'
# print(p.name)
# print(p.surname)


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'Значение {self.__name} должно быть положительным')
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order('apple', 5, 10)
# # apple_order.price = -10
# print(apple_order.total())


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.x)
# p1.x = 5
# print(p1.__dict__)


# Метаклассы (класс, который создаёт другие классы)
# Это классы, экземпляры которого тоже являются классами


# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)


# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

