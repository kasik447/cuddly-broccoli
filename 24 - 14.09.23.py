# from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещён на у2е4")
#
#
# # q = Chess()
# q = Queen()
# q.move()
# q.draw()


# from abc import ABC, abstractmethod


# class Currency(ABC):
#     rub = 'RUB'
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_money(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_money(self):
#         return round(self.value * Dollar.rate_to_rub, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, '=', self.convert_to_money(), Currency.rub)
#
#
# class Euro(Currency):
#     rate_to_eur = 90.14
#     suffix = 'EUR'
#
#     def convert_to_money(self):
#         return round(self.value * Euro.rate_to_eur, 2)
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, '=', self.convert_to_money(), Currency.rub)
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
#
# print('*' * 50)
# for elem in d:
#     elem.print_value()
# print('*' * 50)
# for elem1 in e:
#     elem1.print_value()
# print('*' * 50)


# Интерфейс


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child display1')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild display2')
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()


# Вложенные классы


# class MyOuter:
#     age = 10
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print('Статический метод')
#
#     def obj_method(self):
#         print('Метод экземпляра')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Вложенный класс')
#             print(MyOuter.age)
#             MyOuter.outer_method()
#             print(self.obj.name)
#             self.obj.obj_method()
#
#
# out = MyOuter('Внешний')
# print(out.name)
# inner = out.MyInner('Внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#
#         def display(self):
#             print('Name', self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Intern:
#     def __init__(self):
#         self.name = 'Smith'
#
#     def display(self):
#         print('Name:', self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#
#         def display(self):
#             print('Name:', self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
#
# d1.display()
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Outer show')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print('Inner show')
#
#         class InnerClass:
#             def show(self):
#                 print('InnerClass show')
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show() self.CPU(

class Computer:
    def __init__(self):
        self.name = 'PC001'
        # self.os = self.OS()
        # self.cpu =)

    class OS:
        def system(self):
            return 'Windows 10'

    class CPU:
        def make(self):
            return 'Intel'

        def model(self):
            return 'Core-i9'


comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
my_os = Computer.OS()
my_cpu = Computer.CPU()
print(comp.name)
print(my_os.system())
print(my_cpu.make())
print(my_cpu.model())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self._coord = args
#
#     def __len__(self):
#         return len(self._coord)
#
#
# p = Point(5, 7)
# print(len(p))


# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, v):
#         self.__length = v
#
#
# pt = Point(10, 12)
# print(pt.length)
# # print(pt.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'x', 'y', 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# # print(pt3.__dict__)


