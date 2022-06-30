# pip install flask
from flask import Flask, render_template, redirect
import requests
import webbrowser
from threading import Timer
import os
import time
import sys

app = Flask(__name__)
data = {}

@app.route("/welcome")
def welcome():
    return render_template("welcome.php", message = "Bienvenue sur Météo ")

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/welcome')
    say_welcome()

def say_welcome():
    sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/input/sensor')
    from sensor import setup, loop
    setup()
    loop()

@app.route("/weather-report")
def weather_report():
    sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/traitement')
    sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/input/vocal')
    sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/output/vocal')
    
    # sys.path.insert(0, '/Applications/MAMP/htdocs/2022-meteo-it/scripts/traitement')
    from vocal_recognition import getCityFromAudio
    from wttr import askWttr,getWeatherReport
    from TextToSpeech import audioWeatherReport
    
    recorded_city = getCityFromAudio() 
    response = askWttr(recorded_city)
    weather_report = getWeatherReport(response, recorded_city)
    data = weather_report
    
    location = data['location']['value']
    day_average_temperature = data['day_average_temperature']['value'] + data['day_average_temperature']['unit']
    day_min_temperature = data['day_min_temperature']['value'] + data['day_min_temperature']['unit']
    day_max_temperature = data['day_max_temperature']['value'] + data['day_max_temperature']['unit']
    weather_description = data['weather_description']['value']
    humidity = data['humidity']['value'] + data['humidity']['unit']
    wind = data['wind']['value'] + data['wind']['unit']
    rain = data['rain']['value'] + data['rain']['unit']
    
    if (recorded_city):
        audioWeatherReport(data)
    
    return render_template("output.php", 
        location = location,
        day_average_temperature = day_average_temperature,
        day_min_temperature = day_min_temperature,
        day_max_temperature = day_max_temperature,
        weather_description = weather_description,
        humidity = humidity,
        wind = wind,
        rain = rain,
    )

if __name__ == "__main__":
    Timer(1, open_browser).start();
    app.run()