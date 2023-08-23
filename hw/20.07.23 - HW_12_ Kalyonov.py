def decor(funk):  # summa
    def wrap(*args, **kwargs):  # nums
        print('Сумма чисел', *args, '=', funk(*args, **kwargs))
        print('Среднее арифметическое чисел', *args, '=', funk(*args, **kwargs) / len(args))
    return wrap


@decor
def summa(*nums):
    return sum(nums)


summa(2, 3, 3, 4)
