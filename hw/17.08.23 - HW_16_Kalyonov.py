# Homework

import re

s = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3-67@i.ru, 1login@ru.name.ru'

reg = r'[\d*\w*@._-]+@[\d*\w*@._-]+\.[\d*\w*@.]+'
# reg = r'[a-zа-я0-9_.+-]+@[a-z0-9]+\.[a-z0-9-.]+'

print(re.findall(reg, s))
