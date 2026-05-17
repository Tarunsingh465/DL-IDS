import joblib
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    'data',
    'processed',
    'label_encoder.pkl'
)

# Load encoder
encoder = joblib.load(ENCODER_PATH)

print("\nTRAINED ATTACK LABELS:\n")

for index, label in enumerate(encoder.classes_):
    print(f"{index} -> {label}")