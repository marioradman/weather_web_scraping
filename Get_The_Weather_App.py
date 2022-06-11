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
# Main script for this projects. Calls other scripts to collect the data, save it and notify the user.
# ---------------------------------------------------------------------------
# Library imports
import os
import sys
import boto3
import pathlib
# ---------------------------------------------------------------------------
# Own source imports
import src.Email
from src import zamgWebScraping
from src import save_to_csv
from src import getWeatherStationData
from src import Email
# ---------------------------------------------------------------------------


'''if this file is executed via cronjob, it is executed as it is saved in the /home/user directory
therefore it is possible to give the real working directory of this file as a param
this should be done if it is executed as cronjob, otherwise you don't have to input a param
this working directory is saved in the cwd-variable for further usage'''
cwd = ''
args = sys.argv
if len(args) == 2 and os.path.isdir(str(args[1])):
    cwd = str(args[1])
else:
    cwd = str(os.getcwd())

# TODO delete this example if everything with cronjobs is working finde
# see following example if working with files to write them in the working-directory
# path = os.path.join(cwd, "cronTestFile.txt")
# os.system("python " + os.path.join(cwd, "cronTest.py"))

sum_new_enries_zamg_full = 0
sum_new_entries_zamg_sun = 0

for zamg_url in zamgWebScraping.LIST_OF_ZAMG_URLS:
    data_directory = cwd + '/data/'
    try:
        data = zamgWebScraping.zamg_web_scraping(zamg_url)
        if data is None or len(data) == 0:
            raise Exception
    except Exception:
        # deactivate email sending inside AWS
        # src.Email.send_fetching_error_mail('ZAMG')
        sys.exit(1)

    try:
        sum_new_enries_zamg_full += save_to_csv.save_to_file(data[0], save_to_csv.COLUMNS_ZAMG_FULL, prefix='ZAMG_FULL', directory=data_directory)
        sum_new_entries_zamg_sun += save_to_csv.save_to_file(data[1], save_to_csv.COLUMNS_ZAMG_SUN, prefix='ZAMG_SUN', directory=data_directory)
    except Exception as e:
        print(e)
        # deactivate email sending inside AWS
        # src.Email.send_database_error_mail('ZAMG')
        sys.exit(1)

if sum_new_enries_zamg_full == 0 or sum_new_entries_zamg_sun == 0:
    # deactivate email sending inside AWS
    # src.Email.send_zero_entries_import_mail('ZAMG')
    sys.exit(1)

try:
    data = getWeatherStationData.get_weather_station_data()
    if data is None or len(data) == 0:
        raise Exception
except Exception:
    # deactivate email sending inside AWS
    # src.Email.send_fetching_error_mail('PRIVATE_STATION')
    sys.exit(1)

try:
    new_entries_private_station = save_to_csv.save_to_file(data, save_to_csv.COLUMNS_WEATHER_STATION, prefix='PRIVATE_STATION', directory=data_directory)
except Exception:
    # deactivate email sending inside AWS
    # src.Email.send_database_error_mail('PRIVATE_STATION')
    sys.exit(1)

if new_entries_private_station == 0:
    # deactivate email sending inside AWS
    # src.Email.send_zero_entries_import_mail('PRIVATE_STATION')
    sys.exit(1)

# BEGIN: AWS fileupload
# activate inside AWS

# config data
BASE_DIR = pathlib.Path(__file__).parent.resolve()
AWS_REGION = "" # set AWS config
S3_BUCKET_NAME = "" # set AWS config
s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")

# TODO: Improve/generalize/cleanup of fileupload
upload_files(f"{BASE_DIR}/data/ZAMG_FULL_2022-06.csv", S3_BUCKET_NAME)
upload_files(f"{BASE_DIR}/data/ZAMG_SUN_2022-06.csv", S3_BUCKET_NAME)
upload_files(f"{BASE_DIR}/data/PRIVATE_STATION_2022-06.csv", S3_BUCKET_NAME)
# END: AWS fileupload

# deactivate email sending inside AWS
# src.Email.send_success_mail(sum_new_enries_zamg_full, sum_new_entries_zamg_sun, new_entries_private_station)
sys.exit(0)






