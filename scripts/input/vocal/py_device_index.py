import pyaudio
import py_error_handling

with py_error_handling.noalsaerr():
    p = pyaudio.PyAudio()
    nbDevice = p.get_device_count()
    print(nbDevice)
    fichier = open("peripheriques.txt", "w")
    for i in range(nbDevice):
        infoDevice = p.get_device_info_by_index(i)
        fichier.write(str(infoDevice))
        print(infoDevice)
    fichier.close()
