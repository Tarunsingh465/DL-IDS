from ids_app.zero_day_engine.hybrid_detection_engine import (
    HybridDetectionEngine
)

from ids_app.zero_day_engine.zero_day_engine import (
    ZeroDayEngine
)

from ids_app.zero_day_engine.threat_hunting_engine import (
    ThreatHuntingEngine
)


class AnomalyEngine:

    def __init__(self):

        self.hybrid_engine = (
            HybridDetectionEngine()
        )

        self.zero_day_engine = (
            ZeroDayEngine()
        )

        self.threat_hunter = (
            ThreatHuntingEngine()
        )

    # =====================================================
    # FULL ANOMALY ANALYSIS
    # =====================================================

    def analyze(
        self,
        sample,
        anomaly_count=1
    ):

        # -----------------------------------------
        # Hybrid Detection
        # -----------------------------------------

        hybrid_result = (
            self.hybrid_engine.analyze(
                sample
            )
        )

        # -----------------------------------------
        # Risk Assessment
        # -----------------------------------------

        risk_result = (
            self.zero_day_engine.assess_risk(
                hybrid_result
            )
        )

        # -----------------------------------------
        # Threat Hunting
        # -----------------------------------------

        hunting_result = (
            self.threat_hunter.analyze(
                anomaly_count=
                anomaly_count,

                risk_level=
                risk_result[
                    "risk_level"
                ]
            )
        )

        return {

            "hybrid_result":
                hybrid_result,

            "risk_result":
                risk_result,

            "threat_hunting":
                hunting_result
        }