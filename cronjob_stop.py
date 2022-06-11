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
# Deletes a existing cronjob. If no cronjob exists, nothing changes.
# ---------------------------------------------------------------------------
# Library imports
from crontab import CronTab
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------

CRON_ID = "get_weather_app_llpmrm_0222"

cron = CronTab(user=True)
cron_jobs_removed = 0

for job in cron:
    if job.comment == CRON_ID:
        cron.remove(job)
        cron_jobs_removed += 1
        cron.write()

if cron_jobs_removed > 0:
    print("\nNumber of succesfully removed cronjobs: " + str(cron_jobs_removed) + "\n")
else:
    print("\nNo cronjobs have been removed.\n")
