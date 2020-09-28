from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import flix.adapters.repository as repo
import flix.utilities.utilities as utilities
import flix.movies.services as services

from flix.authentication.authentication import login_required

####IGNORE FOR NOW#####
# Configure Blueprint.
news_blueprint = Blueprint('news_bp', __name__)


@movies_blueprint.route('/movies_by_title', methods=['GET'])
def movies_by_title():
    # Read query parameters.
    target_title = request.args.get('title')
    movie_to_show_reviews = request.args.get('view_reviews_for')

    # Fetch the first and last articles in the series.
    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_title is None:
        # No date query parameter, so return articles from day 1 of the series.
        target_title= first_movie['title']

    if movie_to_show_reviews is None:
        # No view-comments query parameter, so set to a non-existent article id.
        movie_to_show_reviews = -1
    else:
        # Convert article_to_show_comments from string to int.
        movie_to_show_reviews = int(movie_to_show_reviews)

    # Fetch article(s) for the target date. This call also returns the previous and next dates for articles immediately
    # before and after the target date.
    movies, previous_title, next_title = services.get_movies_by_title(target_title, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if len(movies) > 0:
        # There's at least one article for the target date.
        if previous_title is not None:
            # There are articles on a previous date, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_movie_url = url_for('movies_bp.movies_by_title', title=previous_title)
            first_movie_url = url_for('movies_bp.movies_by_title', title=first_movie['title'])

        # There are articles on a subsequent date, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_title is not None:
            next_movie_url = url_for('movies_bp.movies_by_title', title=next_title)
            last_movie_url = url_for('movies_bp.movies_by_title', title=last_movie['title'])

        # Construct urls for viewing article comments and adding comments.
        for movie in movies:
            movie['view_reviews_url'] = url_for('movies_bp.movies_by_title', title=target_title, view_reviews_for=movie['id'])
            movie['add_review_url'] = url_for('movies_bp.review_on_movie', movie=movie['id'])

        # Generate the webpage to display the articles.
        return render_template(
            'movies/movies.html',
            title='Movies',
            movies_title=target_title,
            movies=movies,
            selected_movies=utilities.get_selected_movies(len(movies) * 2),
            genre_urls=utilities.get_genres_and_urls(),
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            prev_movie_url=prev_movie_url,
            next_movie_url=next_movie_url,
            show_reviews_for_movie=movie_to_show_reviews
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))
