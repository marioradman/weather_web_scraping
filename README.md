# Web Scraping Weather
## About
### Project
* Created Date: 06.02.2022
* University:   FH Joanneum
* Study:        Mobile Software Development - 2020
* Course:       Scripting - WS21/22
* Group:        Nr. 5

### Authors/Contributors
* [Lukas Linzer](mailto:lukas.linzer@edu.fh-joanneum.at)
* [Matthias Poettler](mailto:matthias.poettler@edu.fh-joanneum.at)
* [Mario Radman](mailto:mario.radman@edu.fh-joanneum.at)

## Usage
### Prerequisites
- You should have installed at least Python 3.9.
  - You can download it here: [Python Download Page](https://www.python.org/downloads/)
- You should have installed git
  - You can download it here: [Git installation guid](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- It's being tested in Linux-Gnome. No guarantee for Windows, Mac or other Linux-Distributions.
- Clone this repository with following command in your command-line-interface (terminal)
  - `git clone https://git-iit.fh-joanneum.at/radmanma20/scripting_05_weather-web-scraping.git`
  - If you don't have access to the repo, please contact the Authors to gain access (this should not be necessary)

### Installation
- Open command line interface (resp. Terminal)
- Go to the root folder (where this README.md is also located)
- Execute following command: `python app_installation.py`

### Start Script
If you want to start the Script, open the terminal and go to the root folder (where this README.md is also located). <br />
Then execute following command: `python Get_The_Weather_App.py`

### Schedule automation to Start Script periodically
If you want that the script is executed periodically via automation, you can create a cronjob. 
You can do this by opening the terminal. 
Then go to the root folder (where this README.md is also located). <br />
Then execute following command: `python cronjob_start.py`
<br /> <br />
The cronjob-script is then guiding you through your options, how often you want to execute the main script.

#### Change an existing cronjob
If you want to change the time period of executing the script, just execute the cronjob_start script again.
It will overwrite the old setting. It can occur, that the first execution of the script after this change is off time.
(because of the change) The second execution onwards should be then again in the expected time-period, you changed to.
<br /><br />
If you want to delete the cronjob fully and don't execute the script automatically anymore, you have to:
Open the terminal in the root folder (where this README.md is also located).<br />
Execute following command: `python cronjob_stop.py`

## Project Details
### Description
This repository contains the "Web Scraping Weather" (WSW) program. 
It is a script, written in python which should get weather data from the internet.
This program is part of the course "Scripting" in 21/22 of "Mobile Software Development".

Goal of this script is to gather current weather data from different sources. The sources can web:
- Web pages of weather stations (ZAMG)
- Web-API of a private weather-station

This script will implement following functionalities (in brackets the corresponding project criteria from the course):
- Fetching data from websites and server (external data source)
  - We are using a Web-API-Endpoint from a private weather station to collect data as JSON file
  - We are scraping through the ZAMG-Page to get weather data for multiple weather stations
- Searching websites for the wanted information (regex)
  - While web-scraping the data from the ZAMG-webpage we are searching the page through the dom-tree to get the correct parts in the html with the weather data
  - While web-scraping through the ZAMG-Page we also need extended regex to get all needed data in a nice tupel
- This data should be converted into a standardized format and stored into a database for possible further usage. (persistence of data)
  - Because data often comes in different formats, with differently named variables/keys this has to be adapted
  - Some information are useless, other information are missing and must be either set by the script by default or calculated from existing data
  - The data should be then saved in a database. We are using as a "database" csv-files we are creating.
- The script should run repeatedly every day or several times a day. (runnable as cronjob)
  - It is the decision of the user, how often the script will run.
- When the data is collected successfully, an email is sent to inform the users of the script, that the script is still running fine. (notifications)
- When the script encountered any issues, there is also an email notification to the users. (notifications)
- The installation and setup script are using various functionalities to make this script usable (e.g. regex, persistence of data)

### Known Issues
When the ZAMG page is slightly changing, the regex must be adapted. Because of this, the notifications should be watched carefully, 
especially in the beginning. When encountering issues (because somebody at ZAMG thought he/she has to add an special sign somewhere), 
the regex of the ZAMG-webscraping must be adapted. <br />
Because of the various possible issues, log-files are created automatically on some places in the code. 
There could be improvement done and an improved logfile for all exceptions, errors and issues created, but this is currently not implemented in this way.
So only some logfiles are created, but nevertheless the user is informed, if a problem happens (or if nothing happens, because of a lack of notifications).