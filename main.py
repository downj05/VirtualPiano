import vp
import time  


soundfont_path = 'electric_piano_1.sf2'

b1 = vp.Piano(soundfont_path, transpose=1)
b1.volume = 128
while True:
	time.sleep(5)