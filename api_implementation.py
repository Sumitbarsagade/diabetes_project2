# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:14:44 2022

@author: siddhardhan
"""


import json
import requests


url = 'https://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {
    
    'pregnancies' : 10,
    'Glucose' : 115,
    'BloodPressure' : 0,
    'SkinThickness' : 0,
    'Insulin' : 0,
    'BMI' : 35.3,
    'DiabetesPedigreeFunction' : 0.137,
    'Age' : 29
    
    }

input_json = json.dumps(input_data_for_model)


response = requests.post(url, data=input_json)


print(response.text)