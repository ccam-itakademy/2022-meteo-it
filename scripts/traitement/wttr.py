import requests
import json
from bs4 import BeautifulSoup as bs
# import os
# import re 
from datetime import datetime

import sys
sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/input/vocal')
from vocal_recognition import text as recorded_city

today = datetime.today().strftime('%Y-%m-%d')
city = 'Paris'

def askWttr(city):
    url = "https://wttr.in/" + city
    querystring = {
        "format":"j1",
        "lang":"fr"
    }
    return requests.request("GET", url, params=querystring)

def getWeatherReport(response):
    response_json = response.text
    json_load = (json.loads(response_json))

    # Get the city with its region and country
    area = json_load['nearest_area']
    location = city + ', ' + json.dumps(area[0]['region'][0]['value']).strip('"') + ', ' + json.dumps(area[0]['country'][0]['value']).strip('"')

    # Get the info for twttr API
    current_weather = json_load['current_condition'][0]
    day_weather = None
    for day in json_load['weather']:
        if day['date'] == today:
            day_weather = day
            break
        else: 
            day_weather = None

    # Create weather report
    weather_report = {}
    weather_report['location'] = {'value': location, 'unit': None}
    weather_report['day_average_temperature'] = {'value' : day_weather['avgtempC'], 'unit': ' °C'}
    weather_report['day_min_temperature'] = {'value': day_weather['mintempC'], 'unit': ' °C'}
    weather_report['day_max_temperature'] = {'value': day_weather['maxtempC'], 'unit' : ' °C'}
    weather_report['weather_code'] = {'value': current_weather['weatherCode'], 'unit': None}
    weather_report['weather_description'] = {'value': current_weather['lang_fr'][0]['value'], 'unit': None}
    weather_report['humidity'] = {'value': current_weather['humidity'], 'unit': ' %'}
    weather_report['wind'] = {'value': current_weather['windspeedKmph'], 'unit': ' km/h'}
    weather_report['rain'] = {'value': current_weather['precipMM'], 'unit': ' mm'}

    return weather_report

response = askWttr(city)
weather_report = getWeatherReport(response)

# Change the output.php -> replaced with flask templating
# output_file = '../../templates/output.php'
# base = os.path.dirname(os.path.abspath(__file__))
# php = open(os.path.join(base, output_file))
# soup = bs(php, 'html.parser')
# for key, value in weather_report.items():
#     old_text = soup.find(id=key)
#     new_text = old_text.find(text=re.compile(old_text.string)).replace_with(weather_report[key]['value'] + (weather_report[key]['unit'] if weather_report[key]['unit'] else ''))
#     with open(output_file, "wb") as f_output:
#         f_output.write(soup.prettify("utf-8"))
