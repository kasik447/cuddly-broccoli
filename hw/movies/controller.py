from view import UserInterface
from model import MoviesModel


class Controller:
    def __init__(self):
        self.movies_model = MoviesModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            movie = self.user_interface.add_user_movie()
            self.movies_model.add_movie(movie)
        elif answer == '2':
            movies = self.movies_model.get_all_movies()
            self.user_interface.show_all_movies(movies)
        elif answer == '3':
            movie_name = self.user_interface.get_user_movie()
            try:
                movie = self.movies_model.get_single_movie(movie_name)
            except KeyError:
                self.user_interface.show_incorrect_name_error(movie_name)
            else:
                self.user_interface.show_single_movie(movie)
        elif answer == '4':
            movie_name = self.user_interface.get_user_movie()
            try:
                name = self.movies_model.remove_article(movie_name)
            except KeyError:
                self.user_interface.show_incorrect_name_error(movie_name)
            else:
                self.user_interface.remove_single_movie(name)
        elif answer == 'q':
            self.movies_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)
