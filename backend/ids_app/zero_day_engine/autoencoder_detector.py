import numpy as np
import joblib

from tensorflow.keras.models import load_model


class AutoencoderDetector:

    def __init__(self):

        self.model = load_model(
            r"D:\DLIDS\models\autoencoder_model.keras"
        )

        self.threshold = joblib.load(
            r"D:\DLIDS\models\reconstruction_threshold.pkl"
        )

    # =====================================================
    # CALCULATE RECONSTRUCTION ERROR
    # =====================================================

    def reconstruction_error(self, sample):

        sample = np.array(
            sample,
            dtype=np.float32
        )

        sample = sample.reshape(1, -1)

        reconstructed = self.model.predict(
            sample,
            verbose=0
        )

        error = np.mean(
            np.square(sample - reconstructed)
        )

        return float(error)

    # =====================================================
    # DETECT ANOMALY
    # =====================================================

    def detect(self, sample):

        error = self.reconstruction_error(
            sample
        )

        if error <= self.threshold:

            status = "NORMAL"

        elif error <= self.threshold * 2:

            status = "ANOMALY"

        else:

            status = "CRITICAL_ANOMALY"

        return {
            "error": round(error, 6),
            "threshold": round(
                float(self.threshold),
                6
            ),
            "status": status
        }