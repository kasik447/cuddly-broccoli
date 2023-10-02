from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None and length is None:
            self._width = width
            self._length = width
        elif radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError('В дочернем классе должен быть определён метод calc_area()')


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self._radius ** 2, 2)


t = SqTable(10, 20)
print(t.__dict__)
print(t.calc_area())
print()
t2 = SqTable(20)
print(t2.__dict__)
print(t2.calc_area())
print()
t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())


# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть определён метод calc_area()')
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(10, 20)
# print(t.__dict__)
# print(t.calc_area())
# print()
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
# print()
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())
