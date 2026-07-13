from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("health_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    age = float(request.form['age'])
    bmi = float(request.form['bmi'])
    bp = float(request.form['bp'])
    glucose = float(request.form['glucose'])

    features = np.array([[age, bmi, bp, glucose]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "High Health Risk"
    else:
        result = "Low Health Risk"

    return render_template("result.html", prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
