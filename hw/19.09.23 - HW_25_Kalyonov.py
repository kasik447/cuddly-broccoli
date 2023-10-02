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
