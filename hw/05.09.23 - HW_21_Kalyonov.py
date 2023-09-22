# Homework

class Area:
    count = 0

    @staticmethod
    def geron_area(a, b, c):
        p = (a + b + c) / 2
        s = (p*(p - a)*(p - b)*(p - c)) ** 0.5
        Area.count += 1
        return f'Площадь треугольника по формуле Герона {a, b, c}: {s}'

    @staticmethod
    def area_base_and_height(a, b):
        s = (a * b) / 2
        Area.count += 1
        return f'Площадь треугольника через основанию и высоту {a, b}: {s}'

    @staticmethod
    def square_area(a):
        s = a ** 2
        Area.count += 1
        return f'Площадь квадрата ({a}): {s}'

    @staticmethod
    def rectangle_area(a, b):
        s = a * b
        Area.count += 1
        return f'Площадь прямоугольника {a, b}: {s}'

    @staticmethod
    def print_count(a):
        a = Area.count
        return f'Количество подсчётов площади: {a}'


a1 = Area()
print('*' * 60)
print(a1.geron_area(3, 4, 5))
print(a1.area_base_and_height(6, 7))
print(a1.square_area(7))
print(a1.rectangle_area(2, 6))
print(a1.print_count(0))
print('*' * 60)
