import unittest
#@unittest.skip("temp disabled")

class TestParser(unittest.TestCase):
	def setUp(self):
		pass

	def test_LoadSpec(self):
		from autoqc import *

		qu = AutoQC()

		#self.assertEqual(result, CommandParser(command))
