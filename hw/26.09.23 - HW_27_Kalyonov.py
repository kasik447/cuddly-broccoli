class Power:
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError(f'{value} должно быть числом')
        self.value = value

    def __call__(self, func):
        def wrap(x, y):
            if not isinstance(x, int) or not isinstance(y, int):
                raise TypeError(f'{x} и {y} должны быть числами')
            print(f'Результат: {(x * y) ** self.value}')

        return wrap


@Power(3)
def multi(a, b):
    return a * b


multi(2, 2)
