import unittest

from calculator import add, addNewLine, addAllowDelimiters, addDisallowNegative


class TestAdd(unittest.TestCase):

    def test_add(self):
        """Test that it can sum a string of integers"""

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
        """Test that it can sum a string of integers with a new line separator"""

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

    def test_addAllowDelimiters(self):
        """Test that it can sum a string of integers with a specified Delimiter"""

        testCases = {
            47: 0,
            "": 0,
            "1": 0,
            "//;": 0,
            "//;\n": 0,
            "//;\n1;2": 3,
            "//-\n1-20": 21,
            "//a\n4a3": 7,
            "//a\n4aa3": 7,
        }

        for strInput, expectedResult in testCases.items():
            result = addAllowDelimiters(strInput)
            self.assertEqual(result, expectedResult)

    def test_addDisallowNegative(self):
        """Test that it can sum a string of integers with a specified Delimiter and negative numbers not allowed."""

        positiveTestCases = {
            47: 0,
            "": 0,
            "1": 0,
            "//;": 0,
            "//;\n": 0,
            "//;\n1;2": 3,
            "//-\n1-20": 21,
            "//a\n4a3": 7,
            "//a\n4aa3": 7,
        }

        for strInput, expectedResult in positiveTestCases.items():
            result = addAllowDelimiters(strInput)
            self.assertEqual(result, expectedResult)

        negativeTestCases = [
            "//;\n1;-2",
            "//a\n-4a3",
            "//a\n-4a-3",
        ]

        for strInput in negativeTestCases:
            with self.assertRaises(Exception):
                _ = addDisallowNegative(strInput)


if __name__ == "__main_":
    unittest.main()
