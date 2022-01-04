# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    FLASK_ENV = os.getenv("FLASK_ENV")

    if FLASK_ENV == "development":
        return "Starting in development mode..."

    elif FLASK_ENV == "production" or FLASK_ENV is None:
        return "Starting in production mode..."

if __name__ == "__main__":
    print(start())
