import unittest

from calculator import add, addNewLine


class TestAdd(unittest.TestCase):

    def test_add(self):
        """ Test that it can sum a string of integers """

        strInput = 47
        result = add(strInput)
        self.assertEqual(result, 0)

        strInput = ""
        result = add(strInput)
        self.assertEqual(result, 0)
        
        strInput = "1"
        result = add(strInput)
        self.assertEqual(result, 1)
        
        strInput = "1,5"
        result = add(strInput)
        self.assertEqual(result, 6)
    
    def test_addNewLine(self):
        """ Test that it can sum a string of integers with a new line separator """
        strInput = 47
        result = add(strInput)
        self.assertEqual(result, 0)

        strInput = ""
        result = addNewLine(strInput)
        self.assertEqual(result, 0)
        
        strInput = "1"
        result = addNewLine(strInput)
        self.assertEqual(result, 1)
        
        strInput = "1,5"
        result = addNewLine(strInput)
        self.assertEqual(result, 6)
        
        strInput = "1\n2,3"
        result = addNewLine(strInput)
        self.assertEqual(result, 6)
        
        strInput = "1\n2\n4"
        result = addNewLine(strInput)
        self.assertEqual(result, 7)

if __name__ == "__main_":
    unittest.main()