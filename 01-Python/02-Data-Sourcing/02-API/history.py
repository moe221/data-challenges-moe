# pylint: disable=missing-docstring

import sys
import requests
from calendar import monthrange
import pandas as pd

from weather import search_city

BASE_URI = "https://www.metaweather.com"

def daily_forecast(woeid, year, month, day):
    response = requests.get(f"{BASE_URI}/api/location/{woeid}/{year}/{month}/{day}/")
    return response.json()


def monthly_forecast(woeid, year, month):
    """ return a `list` of forecasts for the whole month """
    results = []
    for day in range(1, monthrange(year=year, month=month)[1] + 1):
        response = requests.get(f"{BASE_URI}/api/location/{woeid}/{year}/{month}/{day}")
        results.append(response.json())

    results = [item for sublist in results for item in sublist]
    return results


def write_csv(woeid, year, month, city, forecasts):
    """ dump all the forecasts to a CSV file in the `data` folder """

    df = pd.DataFrame.from_dict(forecasts)
    df.to_csv(f"{year}_{month}_{woeid}_{city}.csv")


def main():
    if len(sys.argv) > 2:
        city = search_city(sys.argv[1])
        if city:
            woeid = city['woeid']
            year = int(sys.argv[2])
            month = int(sys.argv[3])
            if 1 <= month <= 12:
                forecasts = monthly_forecast(woeid, year, month)
                if not forecasts:
                    print("Sorry, could not fetch any forecast")
                else:
                    write_csv(woeid, year, month, city['title'], forecasts)
            else:
                print("MONTH must be a number between 1 (Jan) and 12 (Dec)")
                sys.exit(1)
    else:
        print("Usage: python history.py CITY YEAR MONTH")
        sys.exit(1)


if __name__ == '__main__':
    main()
    #print(monthly_forecast(2487956, 2013, 5))
