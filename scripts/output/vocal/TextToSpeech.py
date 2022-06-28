# Import the required module for text
# to speech conversion
from gtts import gTTS
#import sys
#sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/traitement/')
#from wttr import weather_report as weather_report
print('ok')
def audioWeatherReport(weather_report):
    # The text that you want to convert to audio
    today_meteo = "Aujourd'hui, à {}, il fera en moyenne {} degrés. Nous aurons une température minimale de {} degrés, ainsi qu'une température maximale de {} degrés. Temps prévu : {}. Le taux d'humidité va atteindre les {} pourcent et le vent pourra atteindre les {} kilomètres heure".format(weather_report['location']['value'],weather_report['day_average_temperature']['value'],weather_report['day_min_temperature']['value'],weather_report['day_max_temperature']['value'],weather_report['weather_description']['value'],weather_report['humidity']['value'],weather_report['wind']['value'])


    # Language in which you want to convert
    language = 'fr'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=today_meteo, lang=language, slow=False)

    # Saving the converted audio in a wav file named
    # welcome
    myobj.save("output.mp3")

    # Playing the converted file
    # os.system("mpg321 welcome.mp3")

    from pydub import AudioSegment
    from pydub.playback import play


    song = AudioSegment.from_mp3("output.mp3")
    play(song)
