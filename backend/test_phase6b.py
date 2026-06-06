import numpy as np

from ids_app.zero_day_engine.hybrid_detection_engine import (
    HybridDetectionEngine
)

X_train = np.load(
    r"D:\DLIDS\data\processed\X_train.npy"
)

y_train = np.load(
    r"D:\DLIDS\data\processed\y_train.npy"
)

detector = HybridDetectionEngine()

attack_indices = np.where(
    y_train != 0
)[0]

np.random.shuffle(
    attack_indices
)

TOTAL_ATTACKS = 1000

auto_detect = 0
iso_detect = 0
svm_detect = 0
hybrid_detect = 0

for idx in attack_indices[:TOTAL_ATTACKS]:

    sample = X_train[idx]

    result = detector.analyze(sample)

    if result["autoencoder"]["status"] != "NORMAL":
        auto_detect += 1

    if result["isolation_forest"]["status"] != "NORMAL":
        iso_detect += 1

    if result["one_class_svm"]["status"] != "NORMAL":
        svm_detect += 1

    if result["final_status"] != "NORMAL":
        hybrid_detect += 1

print("\nATTACK BREAKDOWN")
print("Autoencoder:", auto_detect)
print("Isolation Forest:", iso_detect)
print("One-Class SVM:", svm_detect)
print("Hybrid:", hybrid_detect)