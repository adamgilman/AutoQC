import unittest
#@unittest.skip("temp disabled")

class TestObject(unittest.TestCase):
	def setUp(self):
		pass

	def test_LoadObject(self):
		from autoqc import *

		qc = AutoQC()

		#self.assertEqual(result, CommandParser(command))
