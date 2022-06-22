import requests
import json

from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

city = "Marseille"
url = "https://wttr.in/" + city
querystring = {
    "format":"j1",
}

response = requests.request("GET", url, params=querystring)
response_json = response.text

json_load = (json.loads(response_json))
area = json_load['nearest_area']
location = city + ', ' + json.dumps(area[0]['region'][0]['value']).strip('"') + ', ' + json.dumps(area[0]['country'][0]['value']).strip('"')

current_weather = json_load['current_condition'][0]
day_weather = None
for day in json_load['weather']:
    if day['date'] == today:
        day_weather = day
        break
    else: 
        day_weather = None

weather_report = {}
weather_report['location'] = location
weather_report['day_average_temperature'] = day_weather['avgtempC']
weather_report['day_min_temperature'] = day_weather['mintempC']
weather_report['day_max_temperature'] = day_weather['maxtempC']
weather_report['weather_code'] = current_weather['weatherCode']
weather_report['weather_description'] = current_weather['weatherDesc'][0]['value']
weather_report['humidity'] = current_weather['humidity']
weather_report['wind'] = current_weather['windspeedKmph']
weather_report['rain'] = current_weather['precipMM']

print(weather_report)