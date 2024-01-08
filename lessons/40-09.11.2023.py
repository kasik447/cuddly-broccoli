# шаблонизатор Jinja

from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)

per = {"name": "Игорь", "age": 28}

tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
msg = tm.render(p=per)

print(msg)



