import os
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model

# -------------------------------
# SILENCE TF WARNINGS
# -------------------------------
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')


# -------------------------------
# PATH SETUP
# -------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = os.path.join(BASE_DIR, 'models', 'ids_model.keras')
SCALER_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'scaler.pkl')
ENCODER_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'label_encoder.pkl')


# -------------------------------
# LOAD MODEL (SAFE LOAD)
# -------------------------------

model = None
scaler = None
encoder = None

def load_resources():
    global model, scaler, encoder

    if model is None:
        print("🔄 Loading IDS model...")

        model = load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        encoder = joblib.load(ENCODER_PATH)

        print("✅ Model loaded successfully!")


# -------------------------------
# DECISION ENGINE
# -------------------------------

def get_action(label, confidence, threshold=0.8):

    label = label.upper()  # 🔥 FIX

    if confidence < threshold:
        return "MONITOR"

    if label == "BENIGN":
        return "ALLOW"
    else:
        return "BLOCK"


# -------------------------------
# MAIN PREDICTION FUNCTION
# -------------------------------

def predict(features):
    """
    features: list of 78 values
    """

    try:
        # Load model if not loaded
        load_resources()

        # Convert to numpy
        features = np.array(features).reshape(1, -1)

        # Scale
        features_scaled = scaler.transform(features)

        # Predict
        probs = model.predict(features_scaled, verbose=0)[0]

        # Get predicted class
        class_index = np.argmax(probs)
        confidence = float(probs[class_index])

        # Decode label
        predicted_label = encoder.inverse_transform([class_index])[0]

        # Decision logic
        action = get_action(predicted_label, confidence)

        return {
            "predicted_label": predicted_label,
            "confidence": round(confidence, 4),  # cleaner
            "action": action
        }

    except Exception as e:
        print("❌ Prediction Error:", str(e))

        return {
            "predicted_label": "ERROR",
            "confidence": 0.0,
            "action": "MONITOR"
        }