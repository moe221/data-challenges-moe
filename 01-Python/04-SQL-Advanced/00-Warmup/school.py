# pylint:disable=C0111,C0103

import sqlite3


def students_from_city(db, city):
    """return a list of students from a specific city"""

    query = f"""

    SELECT * FROM students
    WHERE students.birth_city = ?

    """

    db.execute(query, (city,))
    return (db.fetchall())


# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py

if __name__ == "__main__":

    conn = sqlite3.connect('data/school.sqlite')
    db = conn.cursor()
    print(students_from_city(db, 'Paris'))
