from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('shablon')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(title="Домашнее задание",
                text="Страница с домашним заданием",
                text1="Домашнее задание выполнено!!!")

print(msg)