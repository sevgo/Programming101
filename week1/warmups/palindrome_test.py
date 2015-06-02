import unittest
from palindrome import palindrome



class Test_Palindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(palindrome("abba_abba"))
        self.assertFalse(palindrome("abba-xabba"))


if __name__ == "__main__":
    unittest.main()
