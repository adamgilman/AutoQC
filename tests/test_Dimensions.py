import unittest
from autoqc import *
#@unittest.skip("temp disabled")

class TestDimensions(unittest.TestCase):
	def setUp(self):
		self.qc = AutoQC()

	def test_DurationIs(self):
		self.qc.load("./tests/fixtures/qc_Valid1080.mp4")
		self.assertEqual( self.qc.DurationIs( "00:00:01.97" ), True )

	def test_bitrate(self):
		self.qc.load("./tests/fixtures/qc_Valid1080.mp4")
		self.assertEqual( self.qc.BitrateIs( "3142" ), True )

	def test_framerate(self):
		self.qc.load("./tests/fixtures/qc_Valid1080.mp4")
		self.assertEqual( self.qc.FramerateIs( "29.97" ), True )


'''	def test_Valid1080(self):
		self.qc.load("fixtures/qc_Valid1080.mp4")
		self.assertTrue( self.qc.ValidDimensions( (1920, 1080) ) )
		#self.assertEqual(result, CommandParser(command))
'''
		
	