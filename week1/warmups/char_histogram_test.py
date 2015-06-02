import unittest
from char_histogram import char_histogram

class Test_CharHistogram(unittest.TestCase):

    def test_ch_occurance(self):
        self.assertIsInstance(char_histogram("Monty Python!"), dict)
        self.assertEqual(char_histogram("montyPython")["o"], 2)


if __name__ == "__main__":
    unittest.main()
