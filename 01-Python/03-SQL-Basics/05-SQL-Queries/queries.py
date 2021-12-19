# pylint: disable=C0103, missing-docstring

import sqlite3


def detailed_movies(db):
    '''return the list of movies with their genres and director name'''

    query = """

    SELECT title, genres, name as director_name FROM movies
    JOIN directors ON
    movies.director_id = directors.id;

    """

    db.execute(query)
    return db.fetchall()


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    query = """

    SELECT title from movies
    JOIN directors ON
    movies.director_id = directors.id
    WHERE start_year > death_year;

    """

    db.execute(query)
    return [title[0] for title in db.fetchall()]


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    query = f"""

    SELECT genres, COUNT(title), ROUND(AVG(minutes), 2) FROM movies
    WHERE genres LIKE '{genre_name}';

    """
    db.execute(query)
    dict_keys = ['genre', 'number_of_movies', 'avg_length']

    return dict(zip(dict_keys, db.fetchall()[0]))


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    query = f"""

    SELECT name, COUNT(title) as movie_count from directors
    JOIN movies ON
    movies.director_id = directors.id
    WHERE movies.genres = '{genre_name}'
    GROUP BY directors.name
    ORDER BY movie_count DESC, name
    LIMIT 5

    """

    db.execute(query)
    return db.fetchall()


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''

    query = """

    SELECT ((minutes / 30) * 30) + 30 AS movie_length, COUNT(title) FROM movies
    WHERE minutes > 0
    GROUP BY movie_length

    """

    db.execute(query)
    return db.fetchall()

def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''

    query = """

    SELECT name, (start_year - birth_year) AS age_when_directed FROM directors
    JOIN movies ON
    movies.director_id = directors.id
    WHERE age_when_directed > 0
    ORDER by age_when_directed ASC
    LIMIT 5

    """
    db.execute(query)
    return db.fetchall()


if __name__ == "__main__":

    conn = sqlite3.connect('data/movies.sqlite')

    # db = conn.cursor()
    # print(top_five_youngest_newly_directors(db))
