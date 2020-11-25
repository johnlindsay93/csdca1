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
        response = self.calculations.calculate_blood_pressure(systolic, diastolic)
        self.assertEqual(response, "Ideal")

    def test_pre_high_bloodpressure_with_lower_diastolic(self):
        systolic = 135
        diastolic = 70
        response = self.calculations.calculate_blood_pressure(systolic, diastolic)
        self.assertEqual(response, "Pre-High")

    def test_pre_high_bloodpressure_with_lower_systolic(self):
        systolic = 110
        diastolic = 85
        response = self.calculations.calculate_blood_pressure(systolic, diastolic)
        self.assertEqual(response, "Pr-High")

    def test_high_bloodpressure_with_lower_diastolic(self):
        systolic = 160
        diastolic = 70
        response = self.calculations.calculate_blood_pressure(systolic, diastolic)
        self.assertEqual(response, "High")

    def test_high_bloodpressure_with_lower_systolic(self):
        systolic = 120
        diastolic = 95
        response = self.calculations.calculate_blood_pressure(systolic, diastolic)
        self.assertEqual(response, "High")


if __name__== "__main__":
    if __name__ == '__main__':
        unittest.main()

