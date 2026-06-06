class ZeroDayEngine:

    def __init__(self):
        pass

    # =====================================================
    # RISK ASSESSMENT
    # =====================================================

    def assess_risk(self, hybrid_result):

        status = hybrid_result["final_status"]

        if status == "NORMAL":

            risk_level = "LOW"

        elif status == "SUSPICIOUS":

            risk_level = "MEDIUM"

        elif status == "HIGH_ANOMALY":

            risk_level = "HIGH"

        elif status == "POTENTIAL_ZERO_DAY":

            risk_level = "POTENTIAL_ZERO_DAY"

        else:

            risk_level = "UNKNOWN"

        return {

            "risk_level": risk_level,

            "hybrid_status": status,

            "anomaly_votes":
                hybrid_result["anomaly_votes"]
        }