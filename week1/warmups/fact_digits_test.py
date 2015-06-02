import unittest
from fact_digits import fact_digits


class Test_Fact_digits(unittest.TestCase):

    def test_fact_digits(self):
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(111), 3)


if __name__ == "__main__":
    unittest.main()
