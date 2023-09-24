# --------------------------------- Вариант 1 ---------------------------------

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт #{self.num} принадлежащий {self.surname} был закрыт')
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#
#         self.print_balance()
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счёте:')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#
#
#
# acc = Account('Долгих', '12345', 0.03, 1000)
# # acc.surname = 'Иванов'
# # print(acc.surname)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
#
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# --------------------------------- Вариант 2 ---------------------------------

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f'Счёт #{self.__num} принадлежащий {self.__surname} был открыт')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.__num} принадлежащий {self.__surname} был закрыт')

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')

        self.print_balance()

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def edit_owner(self, surname):
        self.__surname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')

    def print_balance(self):
        print(f'Текущий баланс: {self.__value} {Account.suffix}')

    def print_info(self):
        print('Информация о счёте:')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

    def set_surname(self, s):
        self.__surname = s

    def get_surname(self):
        return self.__surname

    def set_num(self, n):
        self.__num = n

    def get_num(self):
        return self.__num

    def set_percent(self, p):
        self.__percent = p

    def get_percent(self):
        return self.__percent

    def set_value(self, v):
        self.__value = v

    def get_value(self):
        return self.__value


acc = Account('Долгих', '12345', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()

# acc.edit_owner('Дюма')
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(3000)
print()

acc.withdraw_money(100)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()
