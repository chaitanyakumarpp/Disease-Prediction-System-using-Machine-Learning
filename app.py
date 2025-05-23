# app.py
import csv
from flask import Flask, render_template, request
import model  # This is your model.py

app = Flask(__name__)

# Load symptoms from Testing.csv for dropdown
with open('templates/Testing.csv', newline='') as f:
    reader = csv.reader(f)
    symptoms_list = next(reader)
    symptoms_list = symptoms_list[:-1]

@app.route('/', methods=['GET'])
def home():
    return render_template('includes/default.html', symptoms=symptoms_list)

@app.route('/disease_predict', methods=['POST'])
def disease_prediction():
    selected_symptoms = []
    for i in range(1, 6):
        symptom = request.form.get(f'Symptom{i}')
        if symptom and symptom not in selected_symptoms:
            selected_symptoms.append(symptom)
    
    if not selected_symptoms:
        disease = "No symptoms selected."
    else:
        disease = model.predict_disease(selected_symptoms)

    return render_template('disease_predict.html', disease=disease, symptoms=symptoms_list)

@app.route('/find_doctor', methods=['POST'])
def get_location():
    location = request.form['doctor']
    return render_template('find_doctor.html', location=location, symptoms=symptoms_list)

@app.route('/drug', methods=['POST'])
def find_drug():
    medicine = request.form.get('medicine')
    return render_template('medicine.html', medicine=medicine, symptoms=symptoms_list)

if __name__ == '__main__':
    app.run(debug=True)
