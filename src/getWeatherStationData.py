#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Project:      Weather Web Scraping
# Main:         Get_The_Weather_App
# Created By:   Linzer Lukas, Poettler Matthias, Radman Mario
# Created Date: 06.02.2022
# University:   FH Joanneum
# Study:        Mobile Software Development - 2020
# Course:       Scripting - WS21/22
# Group:        Nr. 5
# Version:      1.0
# ---------------------------------------------------------------------------
# Description of this file
# Collects the Data from the private weather station and parses it into usable format.
# ---------------------------------------------------------------------------
# Library imports
import requests as requests
import json
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------

# prints the weather station data in a correct format - only private use
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# collects the raw weather data from the weather station - only private use
def _collect_raw_weather_station_data():
    response = requests.get("")  # insert credentials
    return response.json()

# parses the raw data into a usable format - only private use
def _parse_raw_weather_station_data(raw_data):
    data = (raw_data["outdoor"]["dew_point"]["value"],
            raw_data["outdoor"]["feels_like"]["value"],
            raw_data["outdoor"]["humidity"]["value"],
            raw_data["pressure"]["absolute"]["value"],
            raw_data["pressure"]["relative"]["value"],
            raw_data["rainfall"]["hourly"]["value"],
            raw_data["solar_and_uvi"]["solar"]["value"],
            raw_data["solar_and_uvi"]["uvi"]["value"],
            raw_data["wind"]["wind_direction"]["value"],
            raw_data["wind"]["wind_gust"]["value"],
            raw_data["wind"]["wind_speed"]["value"])
    return data

# public method which collects, parses and returns the data from the private weather station in the right format
def get_weather_station_data():
    raw_data = _collect_raw_weather_station_data()["data"]
    data = [_parse_raw_weather_station_data(raw_data)]
    return data
