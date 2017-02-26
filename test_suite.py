#/usr/bin/python3 

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
	suite = unittest.TestSuite()

	tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"),\
			TestMathFunc("test_divide")]
	suite.addTests(tests)

	# add single case
	suite.addTest(TestMathFunc("test_multi"))
	# use filename.classname to add all case
	suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
	suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))

	# use class name to load case
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

	# run all test cases and save result to a file
	with open('UnittestReport.txt', 'a') as f:
		runner = unittest.TextTestRunner(stream = f, verbosity = 2)
		runner.run(suite)




