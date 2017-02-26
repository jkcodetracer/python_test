#!/usr/bin/env python3

import unittest

from mathfunc import *

class TestMathFunc(unittest.TestCase):

	""" to set some common environment before running testcases """
	def setUp(self):
		print ("do something before test!")

	def tearDown(self):
		print ("do something after test!")

	def test_add(self):
		self.assertEqual(3, add(1,2))
		self.assertNotEqual(3, add(2,2))
	
	def test_minus(self):
		""" other function: skip(), skipIf() , skipUnless()"""
		self.skipTest("do not run minus")
		self.assertEqual(1, minus(3, 2))

	@unittest.skip("skip function test_multi")
	def test_multi(self):
		self.assertEqual(6, multi(2,3))

	def test_divide(self):
		self.assertEqual(2, divide(6,3))
		self.assertEqual(2.5, divide(5,2))

if __name__ == '__main__':
	unittest.main(verbosity = 2)
