import numpy as np
import joblib


class OneClassSVMDetector:

    def __init__(self):

        self.model = joblib.load(
            r"D:\DLIDS\models\one_class_svm.pkl"
        )

    # =====================================================
    # DETECT
    # =====================================================

    def detect(self, sample):

        sample = np.array(
            sample,
            dtype=np.float32
        ).reshape(1, -1)

        prediction = self.model.predict(sample)

        score = self.model.decision_function(sample)[0]

        if prediction[0] == 1:

            status = "NORMAL"

        else:

            status = "ANOMALY"

        return {
            "status": status,
            "score": round(float(score), 6)
        }