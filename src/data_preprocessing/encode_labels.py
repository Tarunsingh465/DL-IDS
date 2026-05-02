import pandas as pd
from sklearn.preprocessing import LabelEncoder
from feature_selection import select_features
import pickle
import os


def encode_labels(file_name):
    """
    Convert categorical labels into numeric form
    """

    # =========================
    # 1. LOAD FEATURES + LABEL
    # =========================
    X, y = select_features(file_name)

    print("\nOriginal Labels:")
    print(y.unique())

    # =========================
    # 2. LABEL ENCODING
    # =========================
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    print("\nEncoded Labels Sample:")
    print(y_encoded[:10])

    # =========================
    # 3. SHOW MAPPING
    # =========================
    label_mapping = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))

    print("\nLabel Mapping:")
    for k, v in label_mapping.items():
        print(f"{k} → {v}")

    # =========================
    # 4. SAVE ENCODER (IMPORTANT)
    # =========================
    os.makedirs("outputs/processed_data", exist_ok=True)

    with open("outputs/processed_data/label_encoder.pkl", "wb") as f:
        pickle.dump(encoder, f)

    print("\nLabel Encoder saved ✅")

    return X, y_encoded


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    X, y = encode_labels("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("\nEncoding Completed ✅")