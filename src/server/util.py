import json
import pickle
import os
import numpy as np
import warnings
from sklearn.preprocessing import StandardScaler
import pandas as pd

__model=None

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir,'artifacts', 'Diabetes_prediction_model.pickle')

def load_artifacts():
    print('loading saved artifacts....')
    global __model

    with open(model_path,'rb') as f:
        __model=pickle.load(f)
        print('loading complete....') 


def get_prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    input_data = {
        'Pregnancies': [Pregnancies],
        'Glucose': [Glucose],
        'BloodPressure': [BloodPressure],
        'SkinThickness': [SkinThickness],
        'Insulin': [Insulin],
        'BMI': [BMI],
        'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
        'Age': [Age]
    }

    x = pd.DataFrame(input_data)

    prediction = __model.predict(x)
    return "Diabetic" if prediction[0] == 1 else "Not Diabetic"




warnings.filterwarnings("ignore", category=UserWarning, message="Trying to unpickle estimator SVC from version 1.7.0 when using version 1.6.1.*")

load_artifacts()

if __name__=='__main__':
    print(get_prediction(1,85,66,29,0,26.6,0.351,31))    