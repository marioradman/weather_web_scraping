#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Project:      Weather Web Scraping for AWS
# Fork from:    Weather Web Scraping
# Main:         Get_The_Weather_App
# Origin c.b.:  Linzer Lukas, Poettler Matthias, Radman Mario
# Fork c.b.:    Radman Mario
# Created Date: 20.06.2022
# University:   FH Joanneum
# Study:        Mobile Software Development - 2020
# Course:       Web Service Development - SS22
# Version:      1.0
# ---------------------------------------------------------------------------
# This fork of the origin project can only be used within the AWS setup. See the main Readme within the project.
# If you don't know where to search, contact the creators via github.
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
from src import zamgWebScraping
from src import save_to_csv
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

sum_new_enries_zamg_full = 0

for zamg_url in zamgWebScraping.LIST_OF_ZAMG_URLS:
    data_directory = cwd + '/data/'
    try:
        data = zamgWebScraping.zamg_web_scraping(zamg_url)
        if data is None or len(data) == 0:
            raise Exception
    except Exception:
        sys.exit(1)

    try:
        sum_new_enries_zamg_full += save_to_csv.save_to_file(data[0], save_to_csv.COLUMNS_ZAMG_FULL, prefix='ZAMG_FULL', directory=data_directory)
    except Exception as e:
        print(e)
        sys.exit(1)


# BEGIN: AWS fileupload
# config data
BASE_DIR = pathlib.Path(__file__).parent.resolve()
AWS_REGION = "eu-central-1"
S3_BUCKET_NAME = "to-sql-bucket"
s3_client = boto3.client("s3", region_name=AWS_REGION)


def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{file_name}' has been uploaded to '{S3_BUCKET_NAME}'")


# get all created files, pushed it to S3-Bucket and deletes them
files_in_dir = os.listdir('data')
for file_in_dir in files_in_dir:
    if str(file_in_dir) == '.gitkeep':
        continue
    upload_files(f"{BASE_DIR}/data/{file_in_dir}", S3_BUCKET_NAME)
    os.remove(f"{BASE_DIR}/data/{file_in_dir}")

# END: AWS fileupload
sys.exit(0)






