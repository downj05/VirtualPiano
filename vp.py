import keyboard
import time
from mingus.midi import fluidsynth
from mingus.containers.note import Note 


order = [
		'1',
		'!',
		'2',
		'@',
		'3',
		'4',
		'$',
		'5',
		'%',
		'6',
		'^',
		'7',
		'8',
		'*',
		'9',
		'(',
		'0',
		'q',
		'Q',
		"w",
		"W",
		"e",
		"E",
		"r",
		"t",
		"T",
		"y",
		"Y",
		"u",
		"i",
		"I",
		"o",
		"O",
		"p",
		"P",
		"a",
		"s",
		"S",
		"d",
		"D",
		"f",
		"g",
		"G",
		"h",
		"H",
		"j",
		"J",
		"k",
		"l",
		"L",
		"z",
		"Z",
		"x",
		"c",
		"C",
		"v",
		"V",
		"b",
		"B",
		"n",
		"m"
		]

class Piano:
	def __init__(self, soundfont_path, transpose=0, sustain=False):
		self.transposition = transpose
		self.soundfont_path = soundfont_path
		self.order = order
		self.channel = 0
		self.volume_value = 128
		self.pressed_array = [False]*len(order) # Store if a key is pressed to prevent key repetition
		self.sustain = sustain

		self.init()

	def init(self):
		fluidsynth.init(self.soundfont_path)
		keyboard.hook(self.key)

		if self.sustain:
			fluidsynth.control_change(0, 64, 127)
			fluidsynth.control_change(0, 91, 127)
			print("Sustain ON!")
		else:
			fluidsynth.control_change(0, 64, 0)
			fluidsynth.control_change(0, 91, 0)
			print("Sustain OFF!")
		# hooray init noise!
		for octave in range(9):
			fluidsynth.play_Note(Note("C", octave))
			time.sleep(0.1)

	def key(self, callback):
		'''
		If keyboard event is DOWN, play the note and store that the key
		is pressed in the pressed_array. Upon a key UP event, set the key
		to released in the pressed_array to allow future notes.
		'''
		try:
			index = self.order.index(callback.name)
			if callback.event_type == 'down': # If DOWN event
				if self.pressed_array[index] is False: # If key is not pressed
					n = Note().from_int(index+24+self.transposition) # Transpose the note index by 24 semitones so it starts at an acceptable octave
					# We also add/subtract the transposition
					fluidsynth.play_Note(n) # Play note
					self.pressed_array[index] = True # The key is now pressed
					print(f"{callback.name} => {n}")
			else: # UP event
				self.pressed_array[index] = False # Key is released, allow notes

		except Exception as e:
			print(e)

	@property
	def volume(self):
		return self.volume_value

	@volume.setter
	def volume(self, value):
		self.volume_value = value
		fluidsynth.main_volume(self.channel, value)