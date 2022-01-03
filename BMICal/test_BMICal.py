import unittest
import BMICal
import json
from pandas.testing import assert_frame_equal
import pandas as pd

class test_BMICal(unittest.TestCase):
    def test_bmiCalculator(self):
        inputData = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'
        jsonData = json.loads(inputData)  # Convert input string data into json format
        result = BMICal.bmiCalculator(jsonData)
        expectedResult = pd.read_csv('bmical_testresult.csv')
        assert_frame_equal(expectedResult, result)

if __name__ == '__main__':
    unittest.main()