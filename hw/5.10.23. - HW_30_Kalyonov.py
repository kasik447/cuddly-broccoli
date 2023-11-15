import json

data = {}


class CountryCapital:
    @staticmethod
    def add_country(file_name):
        new_country = input('Введите название страны: ')
        new_capital = input('Введите название столицы: ')
        try:
            data1 = json.load(open(file_name))
        except FileNotFoundError:
            data1 = {}
        data1[new_country] = new_capital

        with open(file_name, 'w') as f:
            json.dump(data1, f, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name) as f:
            print(json.load(f))

    @staticmethod
    def delete_country(file_name):
        del_country = input('Введите название страны: ')

        try:
            data1 = json.load(open(file_name))
        except FileNotFoundError:
            data1 = {}

        if del_country in data1:
            del data1[del_country]

            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print('Такой страны в базе нет')

    @staticmethod
    def search_data(file_name):
        try:
            data1 = json.load(open(file_name))
        except FileNotFoundError:
            data1 = {}

        country = input('Введите название страны: ')
        if country in data1:
            print(f'Страна {country} - столица {data1[country]} есть в словаре')
        else:
            print(f'Страны {country} нет в словаре')

    @staticmethod
    def edit_data(file_name):
        try:
            data1 = json.load(open(file_name))
        except FileNotFoundError:
            data1 = {}

        country = input('Введите страну для корректировки: ')
        new_capital = input('Введите новое название столицы: ')

        if country in data1:
            data1[country] = new_capital

            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print(f'Такой страны в базе нет')


file = 'list_capital.json'

while True:
    index = input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n'
                  '4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВвод: ')
    if index == '1':
        CountryCapital.add_country(file)
    elif index == '2':
        CountryCapital.delete_country(file)
    elif index == '3':
        CountryCapital.search_data(file)
    elif index == '4':
        CountryCapital.edit_data(file)
    elif index == '5':
        CountryCapital.load_from_file(file)
    elif index == '6':
        break
    else:
        print('Введён некорректный номер')
