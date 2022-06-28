# pip install flask
from flask import Flask, render_template, redirect
import webbrowser
from threading import Timer
import os

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return render_template("welcome.php", message = "Bienvenue sur Météo ")

def open_browser():
    return webbrowser.open_new('http://127.0.0.1:5000/welcome')

@app.route("/restart")
def restart():
    return redirect("/welcome")

@app.route("/weather-report")
def weather_report():
    import sys
    sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/traitement')
    from wttr import weather_report as weather_report
    data = weather_report
    
    location = data['location']['value']
    day_average_temperature = data['day_average_temperature']['value'] + data['day_average_temperature']['unit']
    day_min_temperature = data['day_min_temperature']['value'] + data['day_min_temperature']['unit']
    day_max_temperature = data['day_max_temperature']['value'] + data['day_max_temperature']['unit']
    weather_description = data['weather_description']['value']
    humidity = data['humidity']['value'] + data['humidity']['unit']
    wind = data['wind']['value'] + data['wind']['unit']
    rain = data['rain']['value'] + data['rain']['unit']

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
