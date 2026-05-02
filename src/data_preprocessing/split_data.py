import numpy as np
from sklearn.model_selection import train_test_split
from scale_features import scale_features
import os


def split_data(file_name):
    """
    Split dataset into train and test sets (stratified)
    """

    # =========================
    # 1. LOAD SCALED DATA
    # =========================
    X, y = scale_features(file_name)

    print("\nTotal Data Shape:", X.shape)

    # =========================
    # 2. TRAIN-TEST SPLIT
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,      # 80% train, 20% test
        random_state=42,
        stratify=y          # VERY IMPORTANT
    )

    # =========================
    # 3. PRINT SHAPES
    # =========================
    print("\nTrain Shape:", X_train.shape)
    print("Test Shape:", X_test.shape)

    # =========================
    # 4. CHECK DISTRIBUTION
    # =========================
    print("\nTrain Label Distribution:")
    unique, counts = np.unique(y_train, return_counts=True)
    print(dict(zip(unique, counts)))

    print("\nTest Label Distribution:")
    unique, counts = np.unique(y_test, return_counts=True)
    print(dict(zip(unique, counts)))

    # =========================
    # 5. SAVE DATA
    # =========================
    os.makedirs("outputs/processed_data", exist_ok=True)

    np.save("outputs/processed_data/X_train.npy", X_train)
    np.save("outputs/processed_data/X_test.npy", X_test)
    np.save("outputs/processed_data/y_train.npy", y_train)
    np.save("outputs/processed_data/y_test.npy", y_test)

    print("\nData saved successfully ✅")

    return X_train, X_test, y_train, y_test


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    split_data("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("\nTrain-Test Split Completed ✅")