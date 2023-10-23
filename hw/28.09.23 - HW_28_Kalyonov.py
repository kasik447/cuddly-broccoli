
from HW_Employee import salaryemployee, hourlyemployee, commissionemployee, payrollsystem

salary = salaryemployee.SalaryEmployee(1, 'Валерий Задорожный', 1500)
hourly = hourlyemployee.HourlyEmployee(2, 'Илья Кромин', 40, 15)
commission = commissionemployee.CommissionEmployee(3, 'Николай Хорольский', 1000, 250)
system = payrollsystem.PayrollSystem()
system.calc([salary, hourly, commission])
