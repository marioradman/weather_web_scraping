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
# Asks the user if he wants to execute the main script automatically periodically and if so in which period.
# Created a cronjob to execute the main script (Get_The_Weather_App.py) in this given period.
# When execute while a cronjob exists, the old one will be overwritten if desired.
# ---------------------------------------------------------------------------
# Library imports
import os
import sys
from crontab import CronTab
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------

CRON_ID = "get_weather_app_llpmrm_0222"

cron_dir = str(os.getcwd())
file = cron_dir + r"/Get_The_Weather_App.py"
cron_command = "python " + file + " " + cron_dir

print("\nThis script sets up a cronjob for the 'Get_The_Weather_App'.\n"
      "With a cronjob the app is executed automatically every certain amount of time.\n"
      "If you already have a cronjob, you can change the time-period now.\n"
      "If you want to stop this automatic execution, please execute the conjob_stop.py script.\n")
print("How often you want to execute this script?")
while True:
    choice = input("Every day: d \n"
                   "Every hour: h \n"
                   "Every xx minutes: xx \n"
                   "I don't wont any changes: q\n"
                   "  >>>  ")

    if choice == "q":
        print("No changes have been made. Script is ending.")
        sys.exit(0)

    if choice == "d" or choice == "h" or isinstance(choice, int):
        break

    try:
        val = int(choice)
        if isinstance(val, int):
            choice = val
            break
        else:
            raise ValueError
    except ValueError:
        print("\nYOUR INPUT IS INVALID\n")

cron = CronTab(user=True)

cronjob_updated = False
for job in cron:
    if job.comment == CRON_ID:
        cron.remove(job)
        break

time_period_confirmation_text = ''
job = cron.new(command=cron_command, comment=CRON_ID)
if choice == "d":
    job.every(1).days()
    time_period_confirmation_text = 'daily'
elif choice == "h":
    job.every(1).hours()
    time_period_confirmation_text = 'hourly'
elif isinstance(choice, int):
    job.minute.every(choice)
    time_period_confirmation_text = 'every ' + str(choice) + ' minutes'
else:
    print("\nERROR: Could not create cronjob. Check if you have enough permissions or your input was correct.")

cron.write()

if cronjob_updated:
    print("\nCrownjob was succesfully updated.")

print("Weather data is now being collected " + time_period_confirmation_text + ".")
