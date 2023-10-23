from lessons.car import carclass


class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, probeg, battery):
        super().__init__(brand, model, year, probeg)
        self.battery = battery

    def description_battery(self):
        print(f'Этот автомобиль имеет мощность {self.battery}%')


if __name__ == '__main__':
    car = ElectroCar('Tesla', 'T', 2018, 99000, 100)
    car.show_car()
    car.description_battery()

