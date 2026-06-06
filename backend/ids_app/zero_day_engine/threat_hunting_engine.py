class ThreatHuntingEngine:

    def __init__(self):
        pass

    # =====================================================
    # HUNT THREATS
    # =====================================================

    def analyze(
        self,
        anomaly_count,
        risk_level
    ):

        # -----------------------------------------
        # Escalation Logic
        # -----------------------------------------

        if risk_level == "POTENTIAL_ZERO_DAY":

            if anomaly_count >= 5:

                threat_level = (
                    "CRITICAL_THREAT"
                )

            elif anomaly_count >= 3:

                threat_level = (
                    "HIGH_RISK"
                )

            else:

                threat_level = (
                    "SUSPICIOUS_ACTIVITY"
                )

        else:

            threat_level = (
                "NORMAL_ACTIVITY"
            )

        return {

            "anomaly_count":
                anomaly_count,

            "risk_level":
                risk_level,

            "threat_level":
                threat_level
        }