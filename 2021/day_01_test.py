import unittest
from day_01 import countMeasurements1, countMeasurements2

class MyTestCase(unittest.TestCase):
    global test_input
    test_input = ["199\n", "200\n", "208\n", "210\n", "200\n", "207\n", "240\n", "269\n", "260\n", "263\n"]

    def test_countMeasurements1(self):
        self.assertEqual(countMeasurements1(test_input), 7)

    def test_countMeasurements2(self):
        self.assertEqual(countMeasurements2(test_input), 5)
