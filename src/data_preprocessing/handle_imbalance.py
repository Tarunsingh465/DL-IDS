import numpy as np
from sklearn.utils.class_weight import compute_class_weight
from split_data import split_data
import pickle
import os


def handle_imbalance(file_name):
    """
    Compute class weights to handle imbalance
    """

    # =========================
    # 1. LOAD TRAIN DATA
    # =========================
    X_train, X_test, y_train, y_test = split_data(file_name)

    print("\nCalculating Class Weights...")

    # =========================
    # 2. COMPUTE CLASS WEIGHTS
    # =========================
    classes = np.unique(y_train)

    class_weights = compute_class_weight(
        class_weight='balanced',
        classes=classes,
        y=y_train
    )

    class_weights_dict = dict(zip(classes, class_weights))

    print("\nClass Weights:")
    for k, v in class_weights_dict.items():
        print(f"Class {k} → Weight {v:.4f}")

    # =========================
    # 3. SAVE CLASS WEIGHTS
    # =========================
    os.makedirs("outputs/processed_data", exist_ok=True)

    with open("outputs/processed_data/class_weights.pkl", "wb") as f:
        pickle.dump(class_weights_dict, f)

    print("\nClass weights saved ✅")

    return class_weights_dict


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    handle_imbalance("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

    print("\nImbalance Handling Completed ✅")