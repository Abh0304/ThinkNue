from flask import Flask, request, render_template, jsonify
import numpy as np
import tensorflow as tf
import joblib
import os

app = Flask(__name__)

# Load model and scaler
MODEL_PATH = 'model.h5'
SCALER_PATH = 'scaler.pkl'

model = tf.keras.models.load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Define the input features
FEATURES = [
    'funding_total_usd', 'funding_rounds', 'milestones',
    'relationships', 'age_first_funding_year', 'age_last_funding_year',
    'has_VC', 'has_angel', 'has_roundA', 'has_roundB', 'has_roundC', 'has_roundD',
    'avg_participants', 'is_top500', 'category_code', 
    'is_software', 'is_web', 'is_mobile', 'is_enterprise',
    'is_advertising', 'is_gamesvideo', 'is_ecommerce',
    'is_biotech', 'is_consulting', 'is_othercategory'
]

@app.route('/')
def home():
    return render_template('startup_predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form.get(f)) for f in FEATURES]
        
        # Feature engineering
        funding_total = data[0]
        age_last_funding = data[5]
        funding_rounds = data[1]
        milestones = data[2]

        funding_velocity = funding_total / (age_last_funding + 1)
        milestone_density = milestones / (funding_rounds + 1)

        data.extend([funding_velocity, milestone_density])

        # Scale input
        input_scaled = scaler.transform([data])

        # Predict
        prediction = model.predict(input_scaled)[0][0]
        success_prob = float(prediction)

        result = {
            'success_probability': round(success_prob, 4),
            'verdict': 'Likely to Succeed' if success_prob > 0.5 else 'Unlikely to Succeed'
        }

        return render_template('startup_predictor.html', prediction=result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template, jsonify
import numpy as np
import tensorflow as tf
import joblib
import os

app = Flask(__name__)

# Load model and scaler
MODEL_PATH = 'model.h5'
SCALER_PATH = 'scaler.pkl'

model = tf.keras.models.load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Define the input features
FEATURES = [
    'funding_total_usd', 'funding_rounds', 'milestones',
    'relationships', 'age_first_funding_year', 'age_last_funding_year',
    'has_VC', 'has_angel', 'has_roundA', 'has_roundB', 'has_roundC', 'has_roundD',
    'avg_participants', 'is_top500', 'category_code', 
    'is_software', 'is_web', 'is_mobile', 'is_enterprise',
    'is_advertising', 'is_gamesvideo', 'is_ecommerce',
    'is_biotech', 'is_consulting', 'is_othercategory'
]

@app.route('/')
def home():
    return render_template('startup_predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form.get(f)) for f in FEATURES]
        
        # Feature engineering
        funding_total = data[0]
        age_last_funding = data[5]
        funding_rounds = data[1]
        milestones = data[2]

        funding_velocity = funding_total / (age_last_funding + 1)
        milestone_density = milestones / (funding_rounds + 1)

        data.extend([funding_velocity, milestone_density])

        # Scale input
        input_scaled = scaler.transform([data])

        # Predict
        prediction = model.predict(input_scaled)[0][0]
        success_prob = float(prediction)

        result = {
            'success_probability': round(success_prob, 4),
            'verdict': 'Likely to Succeed' if success_prob > 0.5 else 'Unlikely to Succeed'
        }

        return render_template('startup_predictor.html', prediction=result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
