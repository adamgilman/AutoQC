import unittest
from autoqc.ffwrapper import FFWrapper
#@unittest.skip("temp disabled")

class TestFFWrapper(unittest.TestCase):
	def setUp(self):
		pass

	def test_FileMustExist(self):
		#self.ff = FFWrapper('fixtures/qc_Valid1080.mp4')
		#self.assertEqual(result, CommandParser(command))
		self.assertRaises(Exception, FFWrapper, 'fixtures/qc_NOEXIST.mp4')
		self.assert_( FFWrapper('./tests/fixtures/qc_Valid1080.mp4') )

class TestFFVideoSpecs(unittest.TestCase):
	def setUp(self):
		self.ff = FFWrapper('./tests/fixtures/qc_Valid1080.mp4')

	def test_Duration(self):
		self.assertEqual( self.ff.duration, "00:00:01.97" )

	def test_Bitrate(self):
		self.assertEqual( self.ff.bitrate, "3142" )

	def test_Framerate(self):
		self.assertEqual( self.ff.framerate, "29.97" )