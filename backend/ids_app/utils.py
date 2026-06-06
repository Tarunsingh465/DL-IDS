# utils.py

import os
import random
import numpy as np
import joblib
import tensorflow as tf

from tensorflow.keras.models import (
    load_model
)

# Import AI security agent
from .ai_agent.security_agent import (
    analyze_threat
)


# -------------------------------
# SILENCE TF WARNINGS
# -------------------------------

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

tf.get_logger().setLevel(
    'ERROR'
)


# -------------------------------
# PATH SETUP
# -------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    'models',
    'ids_model.keras'
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    'data',
    'processed',
    'scaler.pkl'
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    'data',
    'processed',
    'label_encoder.pkl'
)


# -------------------------------
# GLOBAL MODEL RESOURCES
# -------------------------------

model = None
scaler = None
encoder = None


# -------------------------------
# LOAD MODEL RESOURCES
# -------------------------------

def load_resources():

    """
    Load DL model and preprocessing
    resources safely.
    """

    global model
    global scaler
    global encoder

    if model is None:

        print("🔄 Loading IDS model...")

        model = load_model(
            MODEL_PATH
        )

        scaler = joblib.load(
            SCALER_PATH
        )

        encoder = joblib.load(
            ENCODER_PATH
        )

        print(
            "✅ IDS resources loaded successfully!"
        )


# -------------------------------
# RANDOM IP GENERATOR
# -------------------------------

def generate_ip():

    """
    Generate simulated IP address.

    Returns:
    str
    """

    return ".".join(

        str(random.randint(1, 255))

        for _ in range(4)
    )


# -------------------------------
# MAIN PREDICTION FUNCTION
# -------------------------------

def predict(features):

    """
    Predict network traffic and perform
    autonomous AI threat analysis.

    Parameters:
    features (list)

    Returns:
    dict
    """

    try:

        # Load resources
        load_resources()

        # Convert features to numpy
        features = np.array(
            features
        ).reshape(1, -1)

        # Scale features
        features_scaled = scaler.transform(
            features
        )

        # Deep Learning prediction
        probabilities = model.predict(
            features_scaled,
            verbose=0
        )[0]

        # Highest probability index
        class_index = np.argmax(
            probabilities
        )

        # Confidence score
        confidence = float(
            probabilities[class_index]
        )

        # Decode label
        predicted_label = encoder.inverse_transform(
            [class_index]
        )[0]

        # Generate simulated IP
        ip_address = generate_ip()

        # Autonomous AI analysis
        ai_response = analyze_threat(

            ip_address=ip_address,

            attack_type=predicted_label,

            confidence=confidence,
            
            feature_vector=features_scaled
        )

        return ai_response

    except Exception as e:

        print(
            "❌ Prediction Error:",
            str(e)
        )

        return {

            "ip_address":
            "0.0.0.0",

            "original_attack":
            "ERROR",

            "normalized_attack":
            "UNKNOWN_ATTACK",

            "confidence":
            0.0,

            "severity":
            "HIGH",

            "decision":
            "MONITOR",

            "repeat_offender":
            False,

            "attack_count":
            0,

            "unique_attacks":
            [],

            "first_seen":
            None,

            "last_seen":
            None,

            "recommendation":
            (
                "Prediction pipeline failure. "
                "Manual investigation recommended."
            ),

            "explanation":
            str(e)
        }