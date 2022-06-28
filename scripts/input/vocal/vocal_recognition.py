import pyaudio
import wave
import speech_recognition as sr
import py_error_handling
from os.path import exists

from get_mic_index import indexMic

CHUNK = 4*1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 3
MIC_INDEX = indexMic # Index à modifier en fonction de l'index du micro
WAVE_OUTPUT_FILENAME = "record.wav"

if not exists('city.txt') and not exists('record.wav'):
    with py_error_handling.noalsaerr():
        p = pyaudio.PyAudio()   
        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=MIC_INDEX,
                    frames_per_buffer=CHUNK)    
        print("* Enregistrement de la voix")    
        frames = [] 
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK, exception_on_overflow = False)
            frames.append(data) 
        print("* Enregistrement fini")  
        stream.stop_stream()
        stream.close()
        p.terminate()   
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()  
    r = sr.Recognizer()
    with sr.AudioFile('record.wav') as source:
        audio_text = r.listen(source)
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text, language="fr-FR")
            print('Conversion du fichier audio en text...')
            print(text)
            fichier = open("city.txt", "w")
            fichier.write(text)
            fichier.close()
        except:
            print('une erreur technique est survenue, merci de réessayer')