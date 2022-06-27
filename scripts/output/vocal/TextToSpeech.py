# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
mytext = 'Bonjour lequipe Météo PI'

# Language in which you want to convert
language = 'fr'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a wav file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
# os.system("mpg321 welcome.mp3")

from pydub import AudioSegment
from pydub.playback import play


song = AudioSegment.from_mp3("welcome.mp3")
play(song)