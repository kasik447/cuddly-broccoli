from hw.HW_Employee import employee


class SalaryEmployee(employee.Employee):
    """Административные работники имеют фиксированную зарплату"""

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate(self):
        return self.weekly_salary


__author__ = 'Alexandr'
if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__}).')