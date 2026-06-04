# containment_engine.py

"""
========================================================
PHASE 6B — CONTAINMENT ENGINE
========================================================

Purpose:

Manage autonomous containment states.

Responsibilities:

- containment escalation
- isolation tracking
- containment history
- threat containment management
- autonomous defense escalation
"""


from datetime import datetime


class ContainmentEngine:

    def __init__(self):

        # ====================================================
        # ACTIVE CONTAINMENTS
        # ====================================================

        self.active_containments = {}

        # ====================================================
        # CONTAINMENT HISTORY
        # ====================================================

        self.containment_history = []

    # ========================================================
    # DETERMINE CONTAINMENT LEVEL
    # ========================================================

    def determine_containment_level(
        self,
        severity,
        decision
    ):

        if decision == "ALLOW":
            return "NO_CONTAINMENT"

        if decision == "MONITOR":
            return "LOW_CONTAINMENT"

        if decision == "WATCHLIST":
            return "LOW_CONTAINMENT"

        if decision == "TEMP BAN":
            return "MEDIUM_CONTAINMENT"

        if decision == "BLOCK":
            return "CRITICAL_CONTAINMENT"

        return "NO_CONTAINMENT"

    # ========================================================
    # APPLY CONTAINMENT
    # ========================================================

    def apply_containment(
        self,
        ip_address,
        severity,
        decision
    ):

        containment_level = (

            self.determine_containment_level(
                severity,
                decision
            )
        )

        containment_record = {

            "ip_address":
            ip_address,

            "severity":
            severity,

            "decision":
            decision,

            "containment_level":
            containment_level,

            "timestamp":
            str(datetime.now())
        }

        self.active_containments[
            ip_address
        ] = containment_record

        self.containment_history.append(
            containment_record
        )

        return containment_record

    # ========================================================
    # RELEASE CONTAINMENT
    # ========================================================

    def release_containment(
        self,
        ip_address
    ):

        if ip_address in self.active_containments:

            del self.active_containments[
                ip_address
            ]

            self.containment_history.append({

                "ip_address":
                ip_address,

                "action":
                "CONTAINMENT_RELEASED",

                "timestamp":
                str(datetime.now())
            })

            return True

        return False

    # ========================================================
    # ACTIVE CONTAINMENTS
    # ========================================================

    def get_active_containments(
        self
    ):

        return self.active_containments

    # ========================================================
    # HISTORY
    # ========================================================

    def get_containment_history(
        self
    ):

        return self.containment_history

    # ========================================================
    # STATISTICS
    # ========================================================

    def get_statistics(
        self
    ):

        return {

            "active_containments":
            len(
                self.active_containments
            ),

            "total_events":
            len(
                self.containment_history
            )
        }


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    engine = ContainmentEngine()

    result = engine.apply_containment(

        ip_address="192.168.1.100",

        severity="CRITICAL",

        decision="BLOCK"
    )

    print("\nContainment:\n")

    print(result)

    print("\nStatistics:\n")

    print(
        engine.get_statistics()
    )