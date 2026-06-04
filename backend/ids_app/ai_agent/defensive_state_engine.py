# defensive_state_engine.py

"""
========================================================
PHASE 6 — DEFENSIVE STATE ENGINE
========================================================

This module controls the global
AI cyber-defense posture/state.

Purpose:
✔ adaptive cyber defense
✔ global threat posture
✔ AI defense escalation
✔ SOC-style emergency states
✔ autonomous platform behavior

The system dynamically changes
its defense mode depending on:

✔ attack severity
✔ attacker reputation
✔ active bans
✔ blocked attackers
✔ threat intensity
========================================================
"""


class DefensiveStateEngine:

    def __init__(self):

        """
        ====================================================
        CURRENT GLOBAL DEFENSE STATE
        ====================================================
        """

        self.current_state = "NORMAL MODE"

    # ====================================================
    # DETERMINE GLOBAL DEFENSIVE STATE
    # ====================================================

    def evaluate_defense_state(

        self,

        critical_attackers,
        blocked_ips,
        temp_banned_ips,
        suspicious_attackers
    ):

        """
        Determine global defense posture.

        Parameters:
        critical_attackers (int)
        blocked_ips (int)
        temp_banned_ips (int)
        suspicious_attackers (int)

        Returns:
        str
        """

        # ------------------------------------------------
        # CRITICAL LOCKDOWN MODE
        # ------------------------------------------------

        if (

            critical_attackers >= 3
            or
            blocked_ips >= 5
        ):

            self.current_state = (
                "CRITICAL LOCKDOWN MODE"
            )

        # ------------------------------------------------
        # DEFENSE MODE
        # ------------------------------------------------

        elif (

            critical_attackers >= 1
            or
            blocked_ips >= 1
            or
            temp_banned_ips >= 3
        ):

            self.current_state = (
                "DEFENSE MODE"
            )

        # ------------------------------------------------
        # ALERT MODE
        # ------------------------------------------------

        elif (

            suspicious_attackers >= 3
            or
            temp_banned_ips >= 1
        ):

            self.current_state = (
                "ALERT MODE"
            )

        # ------------------------------------------------
        # NORMAL MODE
        # ------------------------------------------------

        else:

            self.current_state = (
                "NORMAL MODE"
            )

        return self.current_state

    # ====================================================
    # GET CURRENT STATE
    # ====================================================

    def get_current_state(self):

        return self.current_state