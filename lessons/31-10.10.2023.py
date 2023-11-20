# import csv

# with open('data.csv') as r_file:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         print(f'{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.')
#         count += 1


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 11])
#     writer.writerow(["Маша", 11, 18])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open('sw_data_1.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)


# with open('student_1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

#
# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# with open('todos.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)


# Парсинг сайтов

# pip instal beautifulsoup4 or bs4

# from bs4 import BeautifulSoup


# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find('div', class_='name')  # .text или .string
# row = soup.find_all('div', class_='name')  # .text - не работает
# row = soup.find_all('div', class_='row')[1].find('div', class_='links')  # .text - не работает
# row = soup.find('div', id='salary')
# row = soup.find('div', {'data-set': 'salary'})
# row = soup.find('div', string='Alena')  # text - более старые версии
# row = soup.find('div', string='Alena').parent
# row = soup.find('div', string='Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', class_='row')
# copywriter = []
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)


# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# salary = soup.find_all('div', {'data-set': 'salary'})
# for i in salary:
#     get_salary(i.text)


# import requests

# r = requests.get('https://ru.wordpress.org/')
# print(r.status_code)
# print(r.headers)
# print(r.headers['content-Type'])
# print(r.text)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('section', class_='plugin-section')[1]
    plugins = p1.find_all('article')
    for plugin in plugins:
        name = plugin.find('h3').text
        print(name)


def main():
    url = 'https://ru.wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()



