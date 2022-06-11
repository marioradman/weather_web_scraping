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
# Connects to the mailserver and sends the mail to the desired address of the user.
# ---------------------------------------------------------------------------
# Library imports
import smtplib
import ssl
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------


# sends the mail with the html message
def send_mail(html):
    smtp_server = ""  # insert credentials
    port = 587  # For starttls

    sender_email = ""  # insert credentials
    receiver_email = [""]  # insert credentials
    password = ''  # insert credentials
    today_date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

    # initialise message instance
    msg = MIMEMultipart()
    msg["Subject"] = "Weather Data {}".format(today_date)
    msg["From"] = sender_email
    msg['To'] = ", ".join(receiver_email)

    body_html = MIMEText(html.format(today_date), 'html')  # parse values into html text
    msg.attach(body_html)  # attaching the text body into msg

    context = ssl.create_default_context()
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # check connection
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # check connection
        server.login(sender_email, password)

        # Send email here
        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        try:
            server.quit()
        except Exception as e:
            # Print any error messages to stdout
            print(e)
