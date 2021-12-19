# pylint: disable=missing-docstring, C0103

import sqlite3


def directors_count(db):
    # return the number of directors contained in the database
    db.execute("SELECT COUNT(name) FROM directors;")

    return int(db.fetchall()[0][0])


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db.execute("SELECT name FROM directors ORDER BY name ASC;")

    return [name[0] for name in db.fetchall()]


def love_movies(db):
    # return the list of all movies which contain the word "love" in their title, sorted in alphabetical order
    query = """

    SELECT title FROM movies WHERE title LIKE '%love%'
    ORDER by title ASC;

    """

    db.execute(query)
    return [name[0] for name in db.fetchall()]



def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f"""

    SELECT COUNT(name) FROM directors
    WHERE name LIKE '%{name}%';

    """

    db.execute(query)
    return int(db.fetchall()[0][0])


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration, sorted in the alphabetical order
    query = f"""

    SELECT title FROM movies
    WHERE minutes > {min_length}
    ORDER BY title ASC;

    """

    db.execute(query)
    return [x[0] for x in db.fetchall()]


if __name__  == "__main__":
    pass
    # tests
    # conn = sqlite3.connect('data/movies.sqlite')
    # db = conn.cursor()
    # print(movies_longer_than(db, 20))
