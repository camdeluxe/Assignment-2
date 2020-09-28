from datetime import datetime
from flix.domainmodel.movie import Movie

class Review:
    def __init__(self, movie : Movie, review_text : str, rating : int):
        self.__movie = movie
        self.__review_text = review_text
        if type(rating) == int and (rating >=0 and rating <= 10):
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now().timestamp()

    def __eq__(self, other):
        if self.__movie == other.movie and self.__review_text == other.review_text and self.__rating == other.rating and self.__timestamp == other.timestamp:
            return True
        else:
            return False
    def __repr__(self):
        return f'User gave a rating of {self.__rating} to the movie {self.__movie} with the following review: {self.__review_text}'


    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp


class TestReviewMethods:
    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review1 = Review(movie, review_text, rating)

        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review2 = Review(movie, review_text, rating)

        movie = Movie("Cats", 2016)
        review_text = "This movie was very lame."
        rating = 4
        review3 = Review(movie, review_text, rating)

        assert review1.__eq__(review2) == True
        assert review1.__eq__(review1) == True
        assert review1.__eq__(review3) == False

