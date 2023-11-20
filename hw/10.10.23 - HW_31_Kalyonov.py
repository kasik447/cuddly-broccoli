import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find_all('div', class_='list')[0]
    module = p1.find_all('div', class_='list__item')[1]
    chapter = module.find('a', class_='list__link').text
    sections = module.find_all('a', class_='list-sub__link')

    print(chapter)
    print('-' * 20)

    count = 0
    for section in sections:
        name = section
        count += 1
        print(count, name.text)


def main():
    url = 'https://learn.javascript.ru/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
