# model.py
import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the training data
data = pd.read_csv(os.path.join("templates", "Training.csv"))
symptoms = data.columns[:-1]
prognosis = data['prognosis']

# Prepare data
X = data[symptoms]
y = prognosis

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train the model
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Create a dictionary to map symptoms to index
symptom_index = dict(zip(symptoms, range(len(symptoms))))

def predict_disease(input_symptoms):
    """Predict disease based on user symptoms"""
    input_data = [0] * len(symptoms)
    for symptom in input_symptoms:
        if symptom in symptom_index:
            input_data[symptom_index[symptom]] = 1
    
    input_data = np.array(input_data).reshape(1, -1)
    prediction = dt_model.predict(input_data)
    return prediction[0]
