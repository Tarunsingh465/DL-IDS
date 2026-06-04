# enforcement_policy_engine.py

"""
========================================================
PHASE 6B — ENFORCEMENT POLICY ENGINE
========================================================

Purpose:

Convert AI decisions into
structured enforcement plans.

This simulates how enterprise:

- IPS
- SOAR
- XDR
- SOC platforms

create response policies.
"""


class EnforcementPolicyEngine:

    def __init__(self):

        self.policy_history = []

    # ====================================================
    # GENERATE POLICY
    # ====================================================

    def generate_policy(
        self,
        attack_type,
        severity,
        decision
    ):

        policy = {

            "attack_type":
            attack_type,

            "severity":
            severity,

            "decision":
            decision,

            "ban_duration":
            None,

            "increase_monitoring":
            False,

            "generate_incident":
            False,

            "containment":
            False,

            "defense_escalation":
            False
        }

        # ================================================
        # LOW
        # ================================================

        if severity == "LOW":

            policy[
                "increase_monitoring"
            ] = True

        # ================================================
        # MEDIUM
        # ================================================

        elif severity == "MEDIUM":

            policy[
                "increase_monitoring"
            ] = True

            policy[
                "generate_incident"
            ] = True

        # ================================================
        # HIGH
        # ================================================

        elif severity == "HIGH":

            policy[
                "ban_duration"
            ] = 15

            policy[
                "generate_incident"
            ] = True

            policy[
                "defense_escalation"
            ] = True

        # ================================================
        # CRITICAL
        # ================================================

        elif severity == "CRITICAL":

            policy[
                "ban_duration"
            ] = 60

            policy[
                "generate_incident"
            ] = True

            policy[
                "containment"
            ] = True

            policy[
                "defense_escalation"
            ] = True

        self.policy_history.append(
            policy
        )

        return policy

    # ====================================================
    # HISTORY
    # ====================================================

    def get_policy_history(self):

        return self.policy_history