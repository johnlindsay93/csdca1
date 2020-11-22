import unittest
from calculations import Calculations


class CalculationsTest(unittest.TestCase):

    def setUp(self):
        self.calculations = Calculations()

    def tearDown(self):
        pass

    def test_low_bloodpressure(self):
        systolic = 89
        diastolic = 59
        response = self.calculations.calculate_blood_pressure(systolic, diastolic)
        self.assertEqual(response, "Low")

    def test_ideal_bloodpressure(self):
        systolic = 115
        diastolic = 60
        response = self.calculations.calculate_blood_pressure(systolic,diastolic)
        self.assertEqual(response, "Ideal")


if __name__== "__main__":
    if __name__ == '__main__':
        unittest.main()

