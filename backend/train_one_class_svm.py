import numpy as np
import joblib

from sklearn.svm import OneClassSVM


print("\n====================================================")
print("LOADING TRAINING DATA")
print("====================================================")

X_train = np.load(
    r"D:\DLIDS\data\processed\X_train.npy"
)

y_train = np.load(
    r"D:\DLIDS\data\processed\y_train.npy"
)

print("X_train Shape:", X_train.shape)
print("y_train Shape:", y_train.shape)


# ====================================================
# EXTRACT BENIGN TRAFFIC
# ====================================================

BENIGN_INDEX = 0

X_benign = X_train[y_train == BENIGN_INDEX]

print("\nBENIGN Samples:", len(X_benign))


# ====================================================
# SAMPLE DATA
# ====================================================

sample_size = min(50000, len(X_benign))

indices = np.random.choice(
    len(X_benign),
    sample_size,
    replace=False
)

X_benign = X_benign[indices]

print("Training Samples:", len(X_benign))


# ====================================================
# TRAIN ONE-CLASS SVM
# ====================================================

print("\n====================================================")
print("TRAINING ONE-CLASS SVM")
print("====================================================")

model = OneClassSVM(
    kernel="rbf",
    gamma="scale",
    nu=0.05
)

model.fit(X_benign)

print("\nTraining Complete")


# ====================================================
# SAVE MODEL
# ====================================================

model_path = (
    r"D:\DLIDS\models\one_class_svm.pkl"
)

joblib.dump(
    model,
    model_path
)

print("\nOne-Class SVM Saved")
print("Location:", model_path)

print("\n====================================================")
print("PHASE 7 ONE-CLASS SVM TRAINING COMPLETE")
print("====================================================")