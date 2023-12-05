import pickle
import os.path


class Movies:
    def __init__(self, name, genre, director, year, duration, studio, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.name} - {self.director} - ({self.year})'


class MoviesModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movies(*dict_movie.values())
        self.movies[movie.name] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_name):
        movie = self.movies[user_name]
        dict_movies = {
            'название': movie.name,
            'жанр': movie.genre,
            'режиссер': movie.director,
            'год': movie.year,
            'длительность': movie.duration,
            'студия': movie.studio,
            'актеры': movie.actors
        }
        return dict_movies

    def remove_article(self, movie_name):
        return self.movies.pop(movie_name)

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.movies, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
