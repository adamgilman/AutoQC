import envoy
import os.path

FFMPEG_BIN = "ffmpeg"
FFPROBE_BIN = "ffprobe"

class FFWrapper(object):
	def __init__(self, filename):
		self.ffmpeg = FFMPEG_BIN
		if not os.path.isfile(filename):
			raise Exception("%s does not exist" % filename)
		self.filename = filename

	def probe(self):
		run = envoy.run('ffprobe -i %s' % self.filename)
		output = run.std_out or run.std_err

		return {
					'duration'	:	output.split("Duration: ")[1].split(" ")[0].replace(",", ""),
					'bitrate'	:	output.split("Stream")[1].split("Metadata")[0].split("Video: ")[1].split(",")[4].strip().split(" ")[0],
					'framerate'	:	output.split("Stream")[1].split("Metadata")[0].split("Video: ")[1].split(",")[6].strip().split(" ")[0],
				}

	@property
	def duration(self): return self.probe()['duration']

	@property
	def bitrate(self): return self.probe()['bitrate']
	
	@property
	def framerate(self): return self.probe()['framerate']
	