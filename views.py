from django.shortcuts import render
import joblib
from django.http import JsonResponse
import pandas as pd
import numpy as np
from .models import PatientData
# Load the model
model45 = joblib.load('C:\\Users\\RSV2045\\HDP\\HDproject\\roby\\hd_model\\heart_disease_model.pkl')

# Define a function that will be called when the user visits the /predict
def predict(request):
    try:
        # Get input parameters from the query string
        age = int(request.GET.get('Age',0))
        gender = int(request.GET.get('Gender',0))
        blood_pressure = int(request.GET.get('BloodPressure',0))
        cholesterol = int(request.GET.get('Cholesterol',0))
        heart_rate = int(request.GET.get('HeartRate',0))
        quantum_pattern_feature = float(request.GET.get('QuantumPatternFeature',0.0))

        # Combine inputs into a single list for prediction
        input_data =pd.DataFrame(
             [[age, gender, blood_pressure, cholesterol, heart_rate, quantum_pattern_feature]],
             columns=['Age','Gender','BloodPressure','Cholesterol','HeartRate','QuantumPatternFeature']
        )

        # Make a prediction using the model
        prediction = model45.predict(input_data)[0]  # Extract the first element of the prediction array
        patient_data = PatientData(
            age=age,
            gender=gender,
            blood_pressure=blood_pressure,
            cholesterol=cholesterol,
            heart_rate=heart_rate,
            quantum_pattern_feature=quantum_pattern_feature,
            prediction=prediction 
        )
        patient_data.save()  # Save the patient data to the database
        # Map the prediction to a user-friendly message
        print(f"saving patient data: {patient_data}")
        if prediction == 1:
            message = "The patient is likely to have heart disease."
        else:
            message = "The patient is unlikely to have heart disease."

        # Return the prediction as a JSON response
        return JsonResponse({'prediction': int(prediction), 'message': message})
    except ValueError:
        # Handle invalid input
        return JsonResponse({'error': 'Invalid input. Please provide numeric values for all fields.'}, status=400)
    except Exception as e:
        # Handle unexpected errors
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)

def model(request):
    return render(request, 'index.html')