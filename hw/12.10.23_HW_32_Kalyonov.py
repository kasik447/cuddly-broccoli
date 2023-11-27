from hw_parse_site import Parser


def main():
    pars = Parser('https://www.mk.ru/news/', 'hw_news.txt')
    pars.run()


if __name__ == '__main__':
    main()
