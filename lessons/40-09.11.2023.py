# шаблонизатор Jinja

from jinja2 import Template

# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)

# per = {"name": "Игорь", "age": 28}
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
# msg = tm.render(p=per)
#
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
#
# link = """<select>
# {% for c in cities -%}
#     {% if c.id > 3 -%}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == "Москва" %}
#         <option>{{ c['city'] }}</option>
#     {% else -%}
#         {{ c['city'] }}
#     {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# menu = [
#     {"key": "/index", "atr": "Главная"},
#     {"key": "/news", "atr": "Новости"},
#     {"key": "/about", "atr": "О компании"},
#     {"key": "/shop", "atr": "Магазин"},
#     {"key": "/contacts", "atr": "Контакты"}
# ]
#
# link = '''<ul>
# {% for i in menu-%}
# {% if i["atr"] == "Главная" -%}
#     <li><a href="{{ i["key"] }}" class="active">{{ i["atr"] }}</a></li>
# {% else -%}
#     <li><a href="{{ i["key"] }}">{{ i["atr"] }}</a></li>
# {% endif -%}
# {% endfor -%}
# </ul>'''
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)


# cars = [
# {'model': 'Audi', 'price': 23000},
# {'model': 'Skoda', 'price': 17300},
# {'model': 'Renault', 'price': 44300},
# {'model': 'Wolksvagen', 'price': 21300}
# ]


# tpl = "{{ (cs | min(attribute='price')).model }}"
# tpl = "{{ cs | sort(attribute='price') }}"
# tpl = "{{ cs | random }}"

# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)


# Макроопределения


# html = """
# {% macro input_text(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input_text('username') }}</p>
# <p>{{ input_text('email') }}</p>
# <p>{{ input_text('password') }}</p>
# """
#
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# html = """
# {% macro input_text(type, name, placeholder) -%}
#     <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro %}
#
# <p>{{ input_text('text', 'firstname', 'Имя') }}</p>
# <p>{{ input_text('text', 'lastname', 'Фамилия') }}</p>
# <p>{{ input_text('text', 'address', 'Адрес') }}</p>
# <p>{{ input_text('tel', 'phone', 'Телефон') }}</p>
# <p>{{ input_text('email', 'email', 'Почта') }}</p>
# """
#
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


from jinja2 import Environment, FileSystemLoader


persons = [
    {"name": "Алексей", "year": 18, "weight": 78.5},
    {"name": "Никита", "year": 28, "weight": 82.3},
    {"name": "Виталий", "year": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('shablon')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons, title="About Jinja",
                text="Содержимое сайта")

print(msg)


# from jinja2 import Environment, FileSystemLoader
#
# subs = ["Культура", "Наука", "Политика", "Спорт"]
#
# file_loader = FileSystemLoader('shablon')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('addresses.html')
# msg = tm.render(list_table=subs)
#
# print(msg)


