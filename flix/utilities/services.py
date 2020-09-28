from typing import Iterable
import random

from flix.adapters.repository import AbstractRepository
from flix.domainmodel.movie import Movie


def get_genre_names(repo : AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre for genre in genres]
    return genre_names

def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()

    if quantity >= movie_count:
        # Reduce the quantity of ids to generate if the repository has an insufficient number of articles.
        quantity = movie_count - 1

    # Pick distinct and random articles.
    random_indices = random.sample(range(1, movie_count), quantity)

    random_movies = []
    for index in random_indices:
        random_movies.append(repo.get_movies()[index])


    return random_movies


def movie_to_dict(movie: Movie):
    movie_dict = {
        'title': movie.title,
        'release_year': movie.release_year,
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]
