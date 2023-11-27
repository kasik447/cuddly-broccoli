# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     return re.sub(r'\D+', '', s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         write = csv.writer(f, delimiter=';', lineterminator='\n')
#         write.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[1]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')
#         # url = plugin.find('h3').find('a')['href']
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind_cy(s):
#     return s.split()[-1]
#
#
# def write_scv(data):
#     with open('plugins_2.csv', 'a', encoding='utf-8-sig') as f:
#         write = csv.writer(f, delimiter=';', lineterminator='\r')
#         write.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('article', class_='plugin-card')
#     for el in p1:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#         url = el.find('h3').find('a')['href']
#         snippet = el.find('div', class_='entry-excerpt').text.strip()
#         active = el.find('span', class_='active-installs').text.strip()
#         c = el.find('span', class_='tested-with').text.strip()
#         cy = refind_cy(c)
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_scv(data)
#
#
# def main():
#     for i in range(1, 25):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


from parse_site import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.run()


if __name__ == '__main__':
    main()
