import time
import numpy as np
import tensorflow as tf
import joblib

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint
)


# =========================================================
# START TIMER
# =========================================================

start_time = time.time()


# =========================================================
# LOAD PREPROCESSED TRAINING DATA
# =========================================================

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


# =========================================================
# EXTRACT BENIGN TRAFFIC ONLY
# =========================================================

print("\n====================================================")
print("EXTRACTING BENIGN TRAFFIC")
print("====================================================")

BENIGN_INDEX = 0

X_benign = X_train[y_train == BENIGN_INDEX]

print("BENIGN Samples:", len(X_benign))


# =========================================================
# SAFETY CHECKS
# =========================================================

print("\n====================================================")
print("VERIFYING DATA")
print("====================================================")

print("NaN Count:", np.isnan(X_benign).sum())
print("Inf Count:", np.isinf(X_benign).sum())

print("Max Value:", np.max(X_benign))
print("Min Value:", np.min(X_benign))

# Convert to float32
X_benign = X_benign.astype(np.float32)

print("\nDataset Memory (MB):",
      round(X_benign.nbytes / (1024**2), 2))


# =========================================================
# BUILD AUTOENCODER
# =========================================================

print("\n====================================================")
print("BUILDING AUTOENCODER")
print("====================================================")

input_dim = X_benign.shape[1]

inputs = Input(shape=(input_dim,))

# -------------------------
# Encoder
# -------------------------

x = Dense(64, activation="relu")(inputs)
x = Dense(32, activation="relu")(x)
x = Dense(16, activation="relu")(x)

latent = Dense(
    8,
    activation="relu",
    name="latent_space"
)(x)

# -------------------------
# Decoder
# -------------------------

x = Dense(16, activation="relu")(latent)
x = Dense(32, activation="relu")(x)
x = Dense(64, activation="relu")(x)

outputs = Dense(
    input_dim,
    activation="linear"
)(x)

autoencoder = Model(
    inputs,
    outputs,
    name="ZeroDayAutoencoder"
)

autoencoder.compile(
    optimizer="adam",
    loss="mse"
)

autoencoder.summary()


# =========================================================
# CALLBACKS
# =========================================================

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

checkpoint = ModelCheckpoint(
    r"D:\DLIDS\models\best_autoencoder.keras",
    monitor="val_loss",
    save_best_only=True,
    verbose=1
)


# =========================================================
# TRAIN MODEL
# =========================================================

print("\n====================================================")
print("TRAINING AUTOENCODER")
print("FULL BENIGN DATASET")
print("====================================================")

history = autoencoder.fit(
    X_benign,
    X_benign,
    epochs=20,
    batch_size=2048,
    validation_split=0.10,
    callbacks=[
        early_stop,
        checkpoint
    ],
    verbose=1
)


# =========================================================
# CALCULATE RECONSTRUCTION ERROR
# =========================================================

print("\n====================================================")
print("CALCULATING THRESHOLD")
print("====================================================")

reconstructed = autoencoder.predict(
    X_benign,
    batch_size=4096,
    verbose=1
)

mse = np.mean(
    np.square(X_benign - reconstructed),
    axis=1
)

threshold = np.percentile(
    mse,
    95
)

print("\nReconstruction Threshold:",
      round(float(threshold), 6))


# =========================================================
# SAVE MODEL
# =========================================================

print("\n====================================================")
print("SAVING MODEL")
print("====================================================")

model_path = (
    r"D:\DLIDS\models\autoencoder_model.keras"
)

threshold_path = (
    r"D:\DLIDS\models\reconstruction_threshold.pkl"
)

autoencoder.save(model_path)

joblib.dump(
    float(threshold),
    threshold_path
)

print("\nAutoencoder Saved Successfully")
print("Location:", model_path)

print("\nThreshold Saved Successfully")
print("Location:", threshold_path)


# =========================================================
# TRAINING SUMMARY
# =========================================================

training_time = (
    time.time() - start_time
)

print("\n====================================================")
print("TRAINING SUMMARY")
print("====================================================")

print("BENIGN Samples Used:",
      len(X_benign))

print("Final Training Loss:",
      round(
          float(history.history["loss"][-1]),
          6
      ))

print("Final Validation Loss:",
      round(
          float(history.history["val_loss"][-1]),
          6
      ))

print("Threshold:",
      round(float(threshold), 6))

print("Training Time (minutes):",
      round(training_time / 60, 2))

print("\n====================================================")
print("PHASE 7 FULL-DATA AUTOENCODER TRAINING COMPLETE")
print("====================================================")