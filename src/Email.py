# #!/usr/bin/env python3
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
# Implements the email-templates to notify the user.
# ---------------------------------------------------------------------------
# Library imports
# ---------------------------------------------------------------------------
# Own source imports
from src import SendEmail
# ---------------------------------------------------------------------------


# send success mail with values for sum of new zamg full entries, new zamg sun entries and new private station entries
def send_success_mail(zamg_full_entries, zamg_sun_entries, private_station_entries):
    html = """\
    <html>
      <body>
        <p>Hi,<br>
        <br>
        This is to inform, that the script works fine on {}.<br>
        New created entries for ZAMG_FULL: """ + str(zamg_full_entries) + """<br>\
        New created entries for ZAMG_SUN: """ + str(zamg_sun_entries) + """<br>\
        New created entries for PRIVATE_STATION: """ + str(private_station_entries) + """<br>\
        Have a nice Day. <br>
        </p>
      </body>
    </html>
    """
    SendEmail.send_mail(html)


# send error mail that zero entries have been imported with a text, which component was affected
def send_zero_entries_import_mail(text):
    html = """\
    <html>
      <body>
        <p>Hi,<br>
        <br>
        This is to inform, that there was an Error for creating entries for """ + text + """ on {}.<br>\
        Have a nice Day. <br>
        </p>
      </body>
    </html>
    """
    SendEmail.send_mail(html)


# send error mail that a database error occurred with a text, which component was affected
def send_database_error_mail(text):
    html = """\
    <html>
      <body>
        <p>Hi,<br>
        <br>
        This is to inform, that there was an Error with the database for creating entries for """ + text + """ on {}.<br>\
        Have a nice Day. <br>
        </p>
      </body>
    </html>
    """
    SendEmail.send_mail(html)


# send error mail that a fetching values error occurred with a text, which component was affected
def send_fetching_error_mail(text):
    html = """\
    <html>
      <body>
        <p>Hi,<br>
        <br>
        This is to inform, that there was an fetching values error for """ + text + """ on {}.<br>\
        Have a nice Day. <br>
        </p>
      </body>
    </html>
    """
    SendEmail.send_mail(html)
