# Import the required module for text
# to speech conversion
from gtts import gTTS
import sys
sys.path.insert(0, '/var/www/html/2022-meteo-it/scripts/input/vocal')
from wttr import weather_report as weather_report

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
today_meteo = "Aujourd'hui à {} il fera en moyenne {} degrés. nous aurons une température minimale de {} degrés ainsi qu'une température maximale de {} degrés, temps prévu : {} le taux d'humidité va atteindre les {} pourcent et le vent pourra atteindre les {} kilomètres heure".format(weather_report['location'],weather_report['day_average_temperature'],weather_report['day_min_temperature'],weather_report['day_max_temperature'],weather_report['weather_description'],weather_report['humidity'],weather_report['wind'],)


# Language in which you want to convert
language = 'fr'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=today_meteo, lang=language, slow=False)

# Saving the converted audio in a wav file named
# welcome
myobj.save("Output.mp3")

# Playing the converted file
# os.system("mpg321 welcome.mp3")

from pydub import AudioSegment
from pydub.playback import play


song = AudioSegment.from_mp3("welcome.mp3")
play(song)