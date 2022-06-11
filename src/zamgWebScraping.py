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
# Collects the data from the ZAMG page.
# ---------------------------------------------------------------------------
# Library imports
import re
from urllib import request
from lxml import etree
# ---------------------------------------------------------------------------
# Own source imports
# ---------------------------------------------------------------------------

LIST_OF_ZAMG_URLS = ['https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/vorarlberg/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/tirol/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/salzburg/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/oberoesterreich/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/niederoesterreich/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/wien/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/burgenland/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/kaernten/temperatur/?mode=geo&druckang=red',
                      'https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/steiermark/temperatur/?mode=geo&druckang=red'
                     ]

REGEX_RAW_STATIONS_LIST = r'<tr class="dynPageTableLine.+?</tr>'
REGEX_STATION_INFO = r'red">(.+?)<.+?">([\d\.]+?)<.+?">(?:n\.v\.)?(-?[\d\.]*?)°?(?:&deg;)?<.+?">(?:n\.v\.)?([' \
                     r'\d\.]*?)\s?%?<.+?">(?:n\.v\.)?(\w*?),?\s?([\d\.]*?)(?:\skm/h)?<.+?">\s?(?:n\.v\.)?([\d\.]*?)(' \
                     r'?: km/h)?<.+?">(?:n\.v\.)?([\d\.]*?)\*?\s?<.+?center">(?:n\.v\.)?([\d\.]*?)\*?\s?%?<.+?">(' \
                     r'?:n\.v\.)?(?:k\.A\.)?([\d\.]*?)\s?<(?:.+?Drucktendenz: )?([\w,\s]*)"? '
REGEX_SUN_INFO = r'(?: alt=")(.+?): (.+?)"'

# collects the data from the ZAMG page and returns a tuple of two lists with multiple tuples with the infos.
def zamg_web_scraping(zamg_page_url):
    # fetch the table with values from the page and parse it to string
    with request.urlopen(zamg_page_url) as response:
        html = response.read().decode('utf8')
    root = etree.fromstring(html, etree.HTMLParser())

    # get the element-block and parse it without the rest of the file into a string
    station_elements_list = root.xpath('//table[@class="dynPageTable"]')
    all_stations_string = ''
    for stationElement in station_elements_list:
        all_stations_string += etree.tostring(stationElement, method='html', with_tail=False, encoding='unicode')

    errorLog = ''

    # get the values via regex from the string and save it in list
    raw_stations_list = re.findall(REGEX_RAW_STATIONS_LIST, all_stations_string, re.M)
    stations_list = []
    for rawHtmlStation in raw_stations_list:
        try:
            stations_list.append(re.findall(REGEX_STATION_INFO, rawHtmlStation, re.M)[0])
        except Exception:
            errorLog += 'Could not append station to list: ' + str(rawHtmlStation) + '\n'

    if errorLog != '':
        try:
            file = open('appendErrorLog.txt', 'at')
            file.write(errorLog)
        except Exception:
            print('Could not write file appendErrorLog.')
        finally:
            try:
                file.close()
            except Exception as e:
                print('Error during wiring file appendErrorLog.')

    # get the values for the sun status
    sun_elements_list = root.xpath('//div[@id="overlays"]')
    sun_string = ''
    for sunElements in sun_elements_list:
        sun_string += etree.tostring(sunElements, method='html', with_tail=False, encoding='unicode')
    sun_list = re.findall(REGEX_SUN_INFO, sun_string, re.M)

    return stations_list, sun_list

# method to print the information, commonly used in dev
def _print_station_infos(station_lists_tupel):
    print("NEUES BUNDESLAND\n\n")
    for stationList in station_lists_tupel:
        station_nr = 0
        for station in stationList:
            print("Station " + str(station_nr) + ":")
            print(station)
            print("\n--------------------\n\n")
            station_nr = station_nr + 1
        print("\n" + "="*20 + "\n")
    print("\n\n" + "="*20 + "\n" + "="*20 + "\n" + "="*20 + "\n\n\n\n")

# method to print the information, commonly used in dev
def _count_station_infos(station_lists_tupel):
    print("NEUES BUNDESLAND\n\n")
    for stationList in station_lists_tupel:
        station_nr = 1
        print("Stationlist " + str(station_nr) + ":")
        print(str(len(stationList)))
        station_nr += 1
    print("\n\n" + "="*20 + "\n" + "="*20 + "\n" + "="*20 + "\n\n\n\n")
