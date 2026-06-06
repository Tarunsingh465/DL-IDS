from ids_app.zero_day_engine.autoencoder_detector import (
    AutoencoderDetector
)

from ids_app.zero_day_engine.isolation_forest_detector import (
    IsolationForestDetector
)

from ids_app.zero_day_engine.one_class_svm_detector import (
    OneClassSVMDetector
)


class HybridDetectionEngine:

    def __init__(self):

        self.autoencoder = AutoencoderDetector()

        self.isolation_forest = (
            IsolationForestDetector()
        )

        self.one_class_svm = (
            OneClassSVMDetector()
        )

    # =====================================================
    # HYBRID ANALYSIS
    # =====================================================

    def analyze(self, sample):

        auto_result = (
            self.autoencoder.detect(sample)
        )

        iso_result = (
            self.isolation_forest.detect(sample)
        )

        svm_result = (
            self.one_class_svm.detect(sample)
        )

        anomaly_votes = 0

        if auto_result["status"] != "NORMAL":
            anomaly_votes += 1

        if iso_result["status"] != "NORMAL":
            anomaly_votes += 1

        if svm_result["status"] != "NORMAL":
            anomaly_votes += 1

        # ==========================================
        # DECISION LOGIC
        # ==========================================

        if anomaly_votes == 0:

            final_status = "NORMAL"

        elif anomaly_votes == 1:

            final_status = "SUSPICIOUS"

        elif anomaly_votes == 2:

            final_status = "HIGH_ANOMALY"

        else:

            final_status = "POTENTIAL_ZERO_DAY"

        return {

            "final_status": final_status,

            "anomaly_votes": anomaly_votes,

            "autoencoder": auto_result,

            "isolation_forest": iso_result,

            "one_class_svm": svm_result
        }