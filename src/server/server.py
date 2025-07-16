from flask import Flask,request,jsonify
from flask_cors import CORS
import util


app=Flask(__name__)
CORS(app) 

@app.route('/predict',methods=['POST'])
def predict():
    Pregnancies = float(request.form['prg'])
    Glucose = float(request.form['glc'])
    BloodPressure= float(request.form['bp'])
    SkinThickness= float(request.form['st'])
    Insulin= float(request.form['insulin'])
    BMI= float(request.form['bmi'])
    DiabetesPedigreeFunction= float(request.form['Dpf'])
    Age= float(request.form['age'])

    response = jsonify({
        'prediction':util.get_prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI,DiabetesPedigreeFunction,Age)
    })
    return response

'''
data = request.form
response = jsonify({
    'prediction': util.get_prediction(
        float(data['prg']),
        float(data['glc']),
        float(data['bp']),
        float(data['st']),
        float(data['insulin']),
        float(data['bmi']),
        float(data['Dpf']),
        float(data['age'])
    )
})


'''



if __name__=='__main__':
    app.run(debug=True)
