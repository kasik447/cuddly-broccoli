class PayrollSystem:
    def calc(self, employees):
        print('Расчёт заработной платы')
        print('=' * 50)
        for employee in employees:
            print(f'Заработная плата: {employee.id} - {employee.name}')
            print(f'- Проверить сумму: {employee.calculate()}')
            print()


__author__ = 'Alexandr'
if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__}).')
