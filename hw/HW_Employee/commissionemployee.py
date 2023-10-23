from hw.HW_Employee import salaryemployee


class CommissionEmployee(salaryemployee.SalaryEmployee):
    """Торговые представители, фиксированная зарплата + комиссия"""

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate(self):
        fixed = super().calculate()
        return fixed + self.commission


__author__ = 'Alexandr'
if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__}).')