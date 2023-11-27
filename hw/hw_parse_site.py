import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all('section', class_='news-listing__day-group')[0].find_all('ul', class_='news-listing__day-list')[0]
        li = news.find_all('li', class_='news-listing__item')


        for new in li:
            title = new.find('h3').text
            href = new.find('a').get('href')
            time = new.find('span', class_='news-listing__item-time').text

            self.res.append({
                'title': title,
                'href': href,
                'time': time,
            })

        print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(
                    f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\nВремя: {item["time"]}\n\n{"*" * 20}\n')
                i += 1
