import pyaudio
import py_error_handling

with py_error_handling.noalsaerr():
    p = pyaudio.PyAudio()
    nbDevice = p.get_device_count()
    print(nbDevice)

    for i in range(nbDevice):
        infoDevice = p.get_device_info_by_index(i)
        print(infoDevice)
