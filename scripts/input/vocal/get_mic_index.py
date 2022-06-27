import pyaudio
import py_error_handling

with py_error_handling.noalsaerr():
    p = pyaudio.PyAudio()
    nbDevice = p.get_device_count()
    listPerif = []
    
 
    
    for i in range(nbDevice):
        infoDevice = p.get_device_info_by_index(i)
        listPerif.append(infoDevice)
    
    indexMic = ''

    for perif in listPerif:
        #if perif['name'] == 'USB PnP Sound Device: Audio':
        if 'USB PnP Sound Device: Audio' in perif['name']: 
            indexMic = perif['index']
    
    print("l'index du micro est " + str(indexMic))


