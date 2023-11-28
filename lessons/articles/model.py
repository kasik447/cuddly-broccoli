
class Article:
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self. pages = pages
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.author})'


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):  # {'название': qqq, 'автор': www}
        article = Article(*dict_article.values())  # Article(qqq, www, 3, eee)
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

