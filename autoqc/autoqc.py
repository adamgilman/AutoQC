from ffwrapper import FFWrapper

class AutoQC(object):
	def __init__(self):
		self.ff = None

	def load(self, filename):
		self.ff = FFWrapper(filename)

	def ValidDimensions(self, dimTuple):
		return False

	def DurationIs(self, duration):
		return duration == self.ff.duration

	def BitrateIs(self, bitrate):
		return bitrate == self.ff.bitrate

	def FramerateIs(self, framerate):
		return framerate == self.ff.framerate