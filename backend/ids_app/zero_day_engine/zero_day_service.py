from ids_app.zero_day_engine.anomaly_engine import (
    AnomalyEngine
)

from ids_app.zero_day_engine.anomaly_memory import (
    AnomalyMemory
)

from ids_app.zero_day_engine.zero_day_incident_manager import (
    ZeroDayIncidentManager
)


class ZeroDayService:

    def __init__(self):

        self.anomaly_engine = (
            AnomalyEngine()
        )

        self.memory = (
            AnomalyMemory()
        )

        self.incident_manager = (
            ZeroDayIncidentManager()
        )

    # =====================================================
    # ANALYZE TRAFFIC
    # =====================================================

    def analyze(
        self,
        ip_address,
        sample
    ):

        memory = self.memory.record_anomaly(
            ip_address,
            score=1.0,
            category="ANOMALY"
        )

        anomaly_count = (
            memory["anomaly_count"]
        )

        result = self.anomaly_engine.analyze(
            sample,
            anomaly_count
        )

        risk_level = (
            result["risk_result"][
                "risk_level"
            ]
        )

        incident = None

        if risk_level == (
            "POTENTIAL_ZERO_DAY"
        ):

            incident = (
                self.incident_manager
                .create_incident(
                    ip_address,
                    1.0,
                    risk_level
                )
            )

        return {

            "analysis":
                result,

            "memory":
                memory,

            "incident":
                incident
        }