# pip install flask
from flask import Flask, render_template

import sys
sys.path.insert(0, '/Applications/MAMP/htdocs/2022-meteo-it/scripts/traitement/') # à modifier
from wttr import weather_report as weather_report
data = weather_report.items()
print(data)

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.php", message = "Hello World!")

@app.route("/weather-report")
def weather_report():
    return render_template("output.php", weather_report = data)

if __name__ == "__main__":
    app.run()