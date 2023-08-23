import math
f1 = int(input('1 - прямоугольник, 2 - треугольник, 3 - круг: '))


def rect(h, w):
    r = h * w
    return r


def triangle(foot, h):
    t = foot * h // 2
    return t


def circle(r):
    c = round(math.pi, 2) * (r ** 2)
    return c


if f1 == 1:
    n1 = int(input('Высота: '))
    n2 = int(input('Ширина: '))
    print('Площадь:', rect(n1, n2))
elif f1 == 2:
    n3 = int(input('Основание: '))
    n4 = int(input('Высота: '))
    print('Площадь:', triangle(n3, n4))
elif f1 == 3:
    n5 = int(input('Радиус: '))
    print('Площадь:', circle(n5))
else:
    print('Некорректный ввод данных')
