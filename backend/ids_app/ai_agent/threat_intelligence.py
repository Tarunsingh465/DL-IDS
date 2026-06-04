# threat_intelligence.py

"""
========================================================
PHASE 6 — THREAT INTELLIGENCE ENGINE
========================================================

This module acts as the centralized
AI Threat Intelligence Layer.

Purpose:
✔ track dangerous attackers
✔ maintain attacker intelligence
✔ analyze attack trends
✔ rank threats
✔ provide SOC-style threat visibility
✔ support autonomous AI orchestration
========================================================
"""


class ThreatIntelligenceEngine:

    def __init__(self):

        """
        ====================================================
        ATTACKER DATABASE
        ====================================================

        Stores attacker intelligence profiles.

        Example:
        {
            "192.168.1.10": {
                "attack_count": 5,
                "severity": "HIGH",
                "reputation_score": 80,
                "reputation_level": "HIGH RISK",
                "attacks": ["DDOS", "PORTSCAN"]
            }
        }
        """

        self.attacker_profiles = {}

    # ====================================================
    # UPDATE ATTACKER PROFILE
    # ====================================================

    def update_attacker_profile(
        self,
        ip_address,
        attack_type,
        severity,
        reputation_score,
        reputation_level
    ):

        """
        Update attacker intelligence profile.
        """

        # ----------------------------------------------
        # CREATE NEW PROFILE
        # ----------------------------------------------

        if ip_address not in self.attacker_profiles:

            self.attacker_profiles[ip_address] = {

                "attack_count": 0,

                "severity": severity,

                "reputation_score":
                reputation_score,

                "reputation_level":
                reputation_level,

                "attacks": []
            }

        # ----------------------------------------------
        # UPDATE PROFILE
        # ----------------------------------------------

        profile = self.attacker_profiles[
            ip_address
        ]

        profile["attack_count"] += 1

        profile["severity"] = severity

        profile["reputation_score"] = (
            reputation_score
        )

        profile["reputation_level"] = (
            reputation_level
        )

        # Store unique attacks
        if attack_type not in profile["attacks"]:

            profile["attacks"].append(
                attack_type
            )

    # ====================================================
    # GET ATTACKER PROFILE
    # ====================================================

    def get_attacker_profile(
        self,
        ip_address
    ):

        return self.attacker_profiles.get(
            ip_address,
            {}
        )

    # ====================================================
    # GET TOP ATTACKERS
    # ====================================================

    def get_top_attackers(
        self,
        limit=5
    ):

        """
        Return top dangerous attackers
        ranked by reputation score.
        """

        attackers = list(
            self.attacker_profiles.items()
        )

        # Sort by reputation score
        attackers.sort(

            key=lambda item:
            item[1]["reputation_score"],

            reverse=True
        )

        return attackers[:limit]

    # ====================================================
    # GET CRITICAL ATTACKERS
    # ====================================================

    def get_critical_attackers(self):

        """
        Return all CRITICAL THREAT attackers.
        """

        critical_attackers = {}

        for ip, profile in (
            self.attacker_profiles.items()
        ):

            if (
                profile["reputation_level"]
                ==
                "CRITICAL THREAT"
            ):

                critical_attackers[ip] = profile

        return critical_attackers

    # ====================================================
    # GET TOTAL ATTACKERS
    # ====================================================

    def get_total_attackers(self):

        return len(
            self.attacker_profiles
        )

    # ====================================================
    # GET ATTACK TREND SUMMARY
    # ====================================================

    def get_attack_summary(self):

        """
        Generate basic SOC-style threat summary.
        """

        summary = {

            "total_attackers":
            self.get_total_attackers(),

            "critical_attackers":
            len(
                self.get_critical_attackers()
            ),

            "top_attackers":
            self.get_top_attackers()
        }

        return summary