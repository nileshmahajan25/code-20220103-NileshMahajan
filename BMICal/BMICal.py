import pandas as pd
import json


# Generic function for BMI
def bmiFun(height, weight):
    return round(weight / ((height / 100) ** 2), 1)  # Convert height into meter and calculate BMI


# Generic function for finding BMI range and health risk
def bmiRangeAndRisk(bmiVal):
    if bmiVal <= 18.4:
        return '18.4 and below', 'Malnutrition risk'
    elif bmiVal <= 24.9:
        return '18.5 - 24.9', 'Low risk'
    elif bmiVal <= 29.9:
        return '25 - 29.9', 'Enhanced risk'
    elif bmiVal <= 34.9:
        return '30 - 34.9', 'Medium risk'
    elif bmiVal <= 39.9:
        return '35 - 39.9', 'High risk'
    else:
        return '40 and above', 'Very high risk'


# BMI calculator
# inputData : Input data in list of json data
def bmiCalculator(inputData):
    df = pd.DataFrame.from_records(inputData)  # Convert json (list of json) data to pandas DataFrame
    df['bmi'] = df.apply(lambda row: bmiFun(row.HeightCm, row.WeightKg), axis=1)
    df[['BMI_Range', 'Health_Risk']] = df.apply(lambda row: pd.Series(bmiRangeAndRisk(row.bmi)), axis=1)
    return df
