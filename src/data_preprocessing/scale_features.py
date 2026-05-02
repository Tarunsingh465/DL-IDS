import pandas as pd
from sklearn.preprocessing import StandardScaler
from encode_labels import encode_labels
import pickle
import os


def scale_features(file_name):
    """
    Scale numerical features using StandardScaler
    """

    # =========================
    # 1. LOAD DATA
    # =========================
    X, y = encode_labels(file_name)

    print("\nBefore Scaling:")
    print(X.head())

    # =========================
    # 2. APPLY SCALING
    # =========================
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("\nAfter Scaling (sample):")
    print(X_scaled[:5])

    # =========================
    # 3. SAVE SCALER
    # =========================
    os.makedirs("outputs/processed_data", exist_ok=True)

    with open("outputs/processed_data/scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)

    print("\nScaler saved ✅")

    return X_scaled, y


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    X, y = scale_features("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("\nScaling Completed ✅")