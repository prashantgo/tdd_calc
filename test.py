import unittest

from calculator import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        """ Test that it can sum a string of integers """
        strInput = ""
        result = add(strInput)
        self.assertEqual(result, 0)
        
        strInput = "1"
        result = add(strInput)
        self.assertEqual(result, 1)
        
        strInput = "1,5"
        result = add(strInput)
        self.assertEqual(result, 6)

if __name__ == "__main_":
    unittest.main()