from flix.domainmodel.review import Review
from flix.domainmodel.movie import Movie
from flix.domainmodel.watchlist import WatchList
class User:
    def __init__(self, user_name : str, password : str):
        if type(user_name) == str:
            self.__user_name = user_name.strip().lower()
        else:
            self.__user_name = None
        if type(password) == str:
            self.__password = password
        else:
            self.__password = None
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0
        self.__watchlist = WatchList()

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        if self.__user_name == other.user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__user_name < other.user_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie:Movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review:Review):
        self.__reviews.append(review)
        review.movie.add_review(review)

    def add_movie_to_watchlist(self, movie:Movie):
        self.__watchlist.add_movie(movie)

    def remove_movie_from_watchlist(self, movie: Movie):
        self.__watchlist.remove_movie(movie)

    def select_movie_to_watch(self, index: int):
        return self.__watchlist.select_movie_to_watch(index)

    def get_watchlist_size(self):
        return self.__watchlist.size()

    def get_first_movie_in_watchlist(self):
        return self.__watchlist.first_movie_in_watchlist()

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @property
    def watchlist(self):
        return self.__watchlist


class TestUserMethods:
    def test_init(self):
        user1 = User('Martin', 'pw12345')
        user2 = User('Ian', 'pw67890')
        user3 = User('Daniel', 'pw87465')
        user4 = User('Martin', 'pw1255')
        assert user1.__eq__(user2) == False
        assert user1.__eq__(user1) == True
        assert user1.__eq__(user4) == True
        assert user3.__lt__(user1) == True
        assert user3.__lt__(user3) == False
        assert user1.__lt__(user3) == False

"""
user1 = User('Martin', 'pw12345')
user2 = User('Ian', 'pw67890')
user3 = User('Daniel', 'pw87465')
print(user1)
print(user2)
print(user3)
movie = Movie('Moana', 2016)
movie.runtime_minutes = 56
user1.watch_movie(movie)
print(user1.watched_movies)
print(user1.time_spent_watching_movies_minutes)
user1.add_review(Review(movie, "REVIEW TEXT", 8))
print(user1.reviews)
movie = Movie('F&F', 2001)
movie.runtime_minutes = 112
user1.watch_movie(movie)
print(user1.watched_movies)
print(user1.time_spent_watching_movies_minutes)
user1.add_review(Review(movie, "REVIEW TEXT FOR F&F", 10))
print(user1.reviews)
### new test ###
print("LLLLLLL", movie.reviews)

movie3 = Movie('F&F4', 2007)
user1.add_movie_to_watchlist(movie)
user1.add_movie_to_watchlist(movie3)
print(user1.watchlist)
print(user1.get_watchlist_size())
print(user1.select_movie_to_watch(1))
print(user1.select_movie_to_watch(2))
user1.remove_movie_from_watchlist(movie)
print(user1.watchlist)
"""