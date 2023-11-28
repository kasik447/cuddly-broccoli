from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.articles_model = ArticleModel()  # model
        self.user_interface = UserInterface()  # view

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            article = self.user_interface.add_user_article()
            self.articles_model.add_article(article)
        elif answer == '2':
            articles = self.articles_model.get_all_articles()
            self.user_interface.show_all_articles(articles)