class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def show_point(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError('Операнд должен быть типом Point3D!')
        else:
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError('Операнд должен быть типом Point3D!')
        else:
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError('Операнд должен быть типом Point3D!')
        else:
            return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __floordiv__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError('Операнд должен быть типом Point3D!')
        else:
            return Point3D(self.x // other.x, self.y // other.y, self.z // other.z)

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise ValueError('Операнд должен быть типом Point3D!')
        else:
            return Point3D(self.x == other.x, self.y == other.y, self.z == other.z)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError('Ключ должен быть строкой')

        if item == 'x':
            return f'x = {self.x}'
        if item == 'x1':
            return f'x1 = {self.x}'
        if item == 'y':
            return f'y = {self.y}'
        if item == 'y1':
            return f'y1 = {self.y}'
        if item == 'z':
            return f'z = {self.z}'
        if item == 'z1':
            return f'z1 = {self.z}'

        return 'Неверный ключ'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ должен быть строкой')

        if not isinstance(value, int):
            raise ValueError('Значение должно быть целым числом')

        if key == 'x':
            self.x = value
        if key == 'y':
            self.y = value
        if key == 'z':
            self.z = value


k1 = Point3D(12, 15, 18)
k2 = Point3D(6, 3, 9)

print('Координаты 1-й точки:', k1.show_point())
print('Координаты 2-й точки:', k2.show_point())
k3 = k1 + k2
print(f'Сложение координат: ({k3.show_point()})')
k3 = k1 - k2
print(f'Вычитание координат: ({k3.show_point()})')
k3 = k1 * k2
print(f'Умножение: ({k3.show_point()})')
k3 = k1 // k2
print(f'Деление: ({k3.show_point()})')
print(f'Равенство координат: {k1.show_point() == k2.show_point()}')
print(k1['x'], k2['x1'])
print(k1['y'], k2['y1'])
print(k1['z'], k2['z1'])
print(f'Запись значения в координату x: 20')
k1['x'] = 20
print(k1.show_point())

