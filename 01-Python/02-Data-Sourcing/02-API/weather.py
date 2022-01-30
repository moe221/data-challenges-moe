# pylint: disable=missing-module-docstring

import sys
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates. Return one city (or None)'''
    params = {"query": query}
    response = requests.get(f"{BASE_URI}/api/location/search/", params=params)
    if response.status_code == 200:
        if response.json():
            return response.json()[0]



def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    response = requests.get(f"{BASE_URI}/api/location/{woeid}")
    if response.status_code == 200:
        return response.json()["consolidated_weather"][1::]


def main():
    '''Ask user for a city and display weather forecast'''

    while True:

        query = input("City?\n> ")
        city = search_city(query)

        # if len(result) > 1:
        #     for index, item in enumerate(result):
        #         print(index, item["title"], "\n")

        #     city_id = input("Please enter the correct city number\n> ")
        #     city = result[int(city_id)] if int(city_id) < len(result) else None

        if city is not None:
            break

        print("Error: City not found.\n")

    forecast_list = weather_forecast(city['woeid'])
    for day in forecast_list:
        print(f"{day['applicable_date']}:", day["weather_state_name"],
              f"{round(day['max_temp'], 2)}°C")


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
