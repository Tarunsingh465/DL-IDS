# action_logger.py

"""
========================================================
PHASE 6 — AI ACTION LOGGING ENGINE
========================================================

This module acts as the centralized
AI audit trail system.

Purpose:
✔ log autonomous AI actions
✔ maintain security timelines
✔ store IPS decisions
✔ track defense state changes
✔ provide SOC-style audit trails
✔ support forensic analysis
========================================================
"""

from datetime import datetime


class AIActionLogger:

    def __init__(self):

        """
        ====================================================
        CENTRALIZED ACTION LOG STORAGE
        ====================================================
        """

        self.action_logs = []

    # ====================================================
    # LOG AI ACTION
    # ====================================================

    def log_action(

        self,

        ip_address,
        attack_type,
        severity,
        decision,
        defense_state,
        reputation_level
    ):

        """
        Store autonomous AI action.
        """

        log = {

            "timestamp":
            str(datetime.now()),

            "ip_address":
            ip_address,

            "attack_type":
            attack_type,

            "severity":
            severity,

            "decision":
            decision,

            "defense_state":
            defense_state,

            "reputation_level":
            reputation_level
        }

        self.action_logs.append(log)

    # ====================================================
    # GET ALL LOGS
    # ====================================================

    def get_logs(self):

        return self.action_logs

    # ====================================================
    # GET RECENT LOGS
    # ====================================================

    def get_recent_logs(
        self,
        limit=10
    ):

        return self.action_logs[-limit:]

    # ====================================================
    # GET LOG COUNT
    # ====================================================

    def get_total_logs(self):

        return len(
            self.action_logs
        )

    # ====================================================
    # FILTER BY DECISION
    # ====================================================

    def filter_by_decision(
        self,
        decision
    ):

        filtered_logs = []

        for log in self.action_logs:

            if log["decision"] == decision:

                filtered_logs.append(log)

        return filtered_logs

    # ====================================================
    # FILTER BY SEVERITY
    # ====================================================

    def filter_by_severity(
        self,
        severity
    ):

        filtered_logs = []

        for log in self.action_logs:

            if log["severity"] == severity:

                filtered_logs.append(log)

        return filtered_logs