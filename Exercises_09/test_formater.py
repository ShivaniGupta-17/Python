"""
 Script: test_formater.py
 By: Shivani Gupta (L00171176)
 Tested: Python v3.10.7; Windows 11
 Date: 30th October, 2022
"""

import unittest, formater

class TestFormater(unittest.TestCase):
    def test_lower(self):
        test_text = "SHIVANI"
        result = formater.convert_lower(test_text)
        self.assertEqual(result, "shivani")
    
    def test_upper(self):
        test_text = "Shivani"
        result = formater.convert_upper(test_text)
        self.assertEqual(result, "SHIVANI")

if __name__ =="__main":
    unittest.main()