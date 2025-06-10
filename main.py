import os
import eel
from Backend.features import *
from Backend.command import *

def start():
    eel.init('Frontend')

    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)