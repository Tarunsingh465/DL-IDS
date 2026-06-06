import time
import numpy as np
import joblib

from sklearn.ensemble import IsolationForest


# ====================================================
# START TIMER
# ====================================================

start_time = time.time()


# ====================================================
# LOAD TRAINING DATA
# ====================================================

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

print("\n====================================================")
print("EXTRACTING BENIGN TRAFFIC")
print("====================================================")

BENIGN_INDEX = 0

X_benign = X_train[y_train == BENIGN_INDEX]

print("BENIGN Samples:", len(X_benign))


# ====================================================
# VERIFY DATA
# ====================================================

print("\n====================================================")
print("VERIFYING DATA")
print("====================================================")

print("NaN Count:", np.isnan(X_benign).sum())
print("Inf Count:", np.isinf(X_benign).sum())

print("Max Value:", np.max(X_benign))
print("Min Value:", np.min(X_benign))

X_benign = X_benign.astype(np.float32)

print(
    "\nDataset Memory (MB):",
    round(X_benign.nbytes / (1024**2), 2)
)


# ====================================================
# USE FULL BENIGN DATASET
# ====================================================

print("\n====================================================")
print("USING FULL BENIGN DATASET")
print("====================================================")

print("Training Samples:", len(X_benign))


# ====================================================
# TRAIN ISOLATION FOREST
# ====================================================

print("\n====================================================")
print("TRAINING ISOLATION FOREST")
print("====================================================")

model = IsolationForest(
    n_estimators=200,
    max_samples=500000,
    contamination=0.05,
    random_state=42,
    n_jobs=-1
)
print("Max Samples:", 500000)
model.fit(X_benign)

print("\nTraining Complete")


# ====================================================
# SAVE MODEL
# ====================================================

print("\n====================================================")
print("SAVING MODEL")
print("====================================================")

model_path = (
    r"D:\DLIDS\models\isolation_forest.pkl"
)

joblib.dump(
    model,
    model_path
)

print("\nIsolation Forest Saved")
print("Location:", model_path)


# ====================================================
# TRAINING SUMMARY
# ====================================================

training_time = (
    time.time() - start_time
)

print("\n====================================================")
print("TRAINING SUMMARY")
print("====================================================")

print("BENIGN Samples Used:",
      len(X_benign))

print("Training Time (minutes):",
      round(training_time / 60, 2))

print("\n====================================================")
print("PHASE 7 FULL-DATA ISOLATION FOREST COMPLETE")
print("====================================================")