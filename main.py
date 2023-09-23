import time
import os
import configparser

# Modify path to load fluid synth
app_path = os.getcwd()+r'\fluidsynth'
print(app_path)
if os.environ["PATH"][-1] == '.':
	os.environ["PATH"] = os.environ["PATH"][:-1]
os.environ["PATH"] += ';'+app_path
print(os.environ["PATH"])
import vp

config = configparser.ConfigParser()
config.read('settings.ini')

soundfont_path = config['PIANO']['instrument']
transposition = int(config['PIANO']['transposition'])
sustain = bool(config['PIANO']['sustain'])
volume = int(config['PIANO']['volume'])

b1 = vp.Piano(soundfont_path, transpose=transposition, sustain=sustain)
b1.volume = volume
while True:
	time.sleep(5)