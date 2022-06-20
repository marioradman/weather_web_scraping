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
# Saves given data into a csv-file. Checks if file exists and only appends to existing one.
# Creates one csv-file per prefix (use-case) per month.
# ---------------------------------------------------------------------------
# Library imports
import os
from datetime import datetime
import pandas as pd
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------

COLUMNS_ZAMG_FULL = ['station',
                     'height',
                     'temp',
                     'humidity',
                     'wind-dir',
                     'wind-speed',
                     'wind-max',
                     'rain-mm',
                     'sun-%',
                     'hPa',
                     'p-tendency',
                     'timestamp']
COLUMNS_ZAMG_SUN = ['station',
                    'sun-status',
                    'timestamp']
COLUMNS_WEATHER_STATION = ['dew_point_F',
                           'feels_like_F',
                           'humidity_%',
                           'pressure-abs_mmHg',
                           'pressure-rel_inHg',
                           'rainfall_inH',
                           'solar',
                           'uvi',
                           'wind_direction',
                           'wind_gust_mph',
                           'wind_speed_mph',
                           'timestamp']

# saves the data to a csv file, if the file exists it is only appended, if not a new file is created
# one new file per month and prefix is created
# prefix is optional and can be used to create different files for different use cases
def save_to_file(data, column_names, prefix='', directory='../data/'):
    now = datetime.now()
    if prefix == '':
        file_name = now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"
    else:
        file_name = prefix + "_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"

    df = pd.DataFrame(data)
    df = df.replace('None', '')
    df = df.dropna()
    df['Timestamp'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    df.columns = column_names

    if os.path.exists(directory + file_name) and os.path.isfile(directory + file_name):
        entries_before = sum(1 for line in open(directory + file_name))
        df.to_csv(directory + file_name, mode='a', index=False, encoding="utf-8-sig", header=False, sep=';')
        entries_now = sum(1 for line in open(directory + file_name))
        new_entries = entries_now - entries_before
    else:
        df.to_csv(directory + file_name, mode='a', index=False, encoding="utf-8-sig", header=True, sep=';')
        new_entries = sum(1 for line in open(directory + file_name)) - 1

    return new_entries
