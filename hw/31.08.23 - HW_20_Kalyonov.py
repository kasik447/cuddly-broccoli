# Homework

class Rectangle:

    def __init__(self, long, width):
        # self.__long = self.__width = 0
        self.__long = long
        self.__width = width

    @staticmethod
    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_numbers(self, long, width):
        if Rectangle.__check_value(long) and Rectangle.__check_value(width):
            self.__long = long
            self.__width = width
        else:
            print('Значения должны быть числами!')

    def get_numbers(self):
        print(f'Длинна прямоугольника: {self.__long}')
        print(f'Ширина прямоугольника: {self.__width}')

    def area(self):
        print(f'Площадь прямоугольника: {self.__long * self.__width}')

    def perimeter(self):
        print(f'Периметр прямоугольника: {(self.__long * 2) + (self.__width * 2)}')

    def hypotenuse(self):
        hyp = ((self.__long ** 2) + (self.__width ** 2)) ** 0.5
        print(f'Гипотенуза прямоугольника: {round(hyp, 2)}')

    def drawing_rectangle(self):
        for i in range(self.__long):
            print('*' * self.__width)
        return ''

    def get_long(self):
        return self.__long

    def set_long(self, l):
        if Rectangle.__check_value(l):
            self.__long = l
        else:
            print('"Длинна" должна быть числом!')

    def get_width(self):
        return self.__width

    def set_width(self, w):
        if Rectangle.__check_value(w):
            self.__width = w
        else:
            print('"Ширина" должна быть числом!')


p1 = Rectangle(3, 9)
# p1.set_long(10)
# p1.set_width(23)
p1.get_numbers()
p1.area()
p1.perimeter()
p1.hypotenuse()
print(p1.drawing_rectangle())
