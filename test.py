import unittest

from calculator import add, addNewLine


class TestAdd(unittest.TestCase):

	def test_add(self):
		""" Test that it can sum a string of integers """

		testCases = {
			47: 0,
			"": 0,
			"1": 1,
			"1,5": 6,
		}

		for strInput, expectedResult in testCases.items():
			result = add(strInput)
			self.assertEqual(result, expectedResult)
	
	def test_addNewLine(self):
		""" Test that it can sum a string of integers with a new line separator """

		testCases = {
			47: 0,
			"": 0,
			"1": 1,
			"1,5": 6,
			"1\n2,3": 6,
			"1\n2\n4": 7,
		}

		for strInput, expectedResult in testCases.items():
			result = addNewLine(strInput)
			self.assertEqual(result, expectedResult)

if __name__ == "__main_":
	unittest.main()