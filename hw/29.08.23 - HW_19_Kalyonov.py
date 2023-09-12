# Homework

class Automobile:
    car_make = 'car_make'
    year = '0000'
    brand = 'brand'
    engine_power = 'engine_power'
    color = 'color'
    price = 'price'

    def print_info(self):
        print(' Данные автомобиля '.center(40, '*'))
        print(f'Название модели: {self.car_make}\nГод выпуска: {self.year}\nПроизводитель: {self.brand}'
              f'\nМощность двигателя: {self.engine_power} л.с.\nЦвет машины: {self.color}\nЦена: {self.price}')
        print('=' * 40)

    def input_info(self, car_make, year, brand, engine_power, color, price):
        self.car_make = car_make
        self.year = year
        self.brand = brand
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def set_car_make(self, value):
        self.car_make = value

    def get_car_make(self):
        return self.car_make

    def set_year(self, value):
        self.year = value

    def get_year(self):
        return self.year

    def set_brand(self, value):
        self.brand = value

    def get_brand(self):
        return self.brand

    def set_engine_power(self, value):
        self.engine_power = value

    def get_engine_power(self):
        return self.engine_power

    def set_color(self, value):
        self.color = value

    def get_color(self):
        return self.color

    def set_price(self, value):
        self.price = value

    def get_price(self):
        return self.price


p1 = Automobile()
p1.input_info('X7 M50i', '2021', 'BMW', '530', 'white', '10790000')
p1.print_info()
p1.set_price('12300000')
print(p1.get_price())
p1.set_year('2022')
print(p1.get_year())
