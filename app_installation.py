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
# Installation script. Installs via pip all necessary 3rd party libraries. Must be performed once before doing anything.
# ---------------------------------------------------------------------------
# Library imports
import os
import re
import sys
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------

ALL_INSTALLATION_PACKAGES = ['python-crontab',
                             'datetime',
                             'requests',
                             'pandas',
                             'lxml',
                             'email-to',
                             'boto3',
                             'pathlib']

nr_of_successful_installations = 0

for installation in ALL_INSTALLATION_PACKAGES:
    cl = os.popen('pip install ' + installation + ' 2>&1')
    data = cl.read()
    cl.close()
    error_match = re.search('ERROR:', str(data), re.MULTILINE)

    try:
        file = open("./src/pipLog.txt", "at")
        file.write(str(data))
        file.write("\n\n" + "=" * 32 + "\n" + "=" * 32 + "\n\n\n")
        file.close()
        if error_match is not None:
            raise ImportError
        nr_of_successful_installations += 1
    except Exception:
        sys.stderr.write("\n\nERROR: Installation was UNSUCCESSFUL.\n\n"
                         "Please check your internet connection.\n"
                         "Please check that your python is on version 3.9+\n"
                         "Please check your user permissions.\n"
                         "The error raised during installation of package: " + installation +
                         "If it is still not working, please contact the developers (listed in the Readme).\n\n")

if nr_of_successful_installations == len(ALL_INSTALLATION_PACKAGES):
    print("\n\nINSTALLATION SUCCESSFUL.\n\n")
else:
    print("\n\nERROR: Installation was UNSUCCESSFUL.\n\n")
