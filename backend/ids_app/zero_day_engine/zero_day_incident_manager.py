"""
========================================================
PHASE 7 — ZERO-DAY INCIDENT MANAGER
========================================================

Purpose:
- Manage anomaly investigations
- Track potential zero-day cases
- Maintain investigation lifecycle
"""

from datetime import datetime


class ZeroDayIncidentManager:

    def __init__(self):
        """
        Store all zero-day investigations.
        """
        self.incidents = {}
        self.counter = 1

    def create_incident(
        self,
        ip_address,
        anomaly_score,
        risk_level
    ):
        """
        Create a new zero-day investigation.
        """

        incident_id = f"ZD-{self.counter:05d}"

        incident = {
            "incident_id": incident_id,
            "ip_address": ip_address,
            "anomaly_score": anomaly_score,
            "risk_level": risk_level,
            "status": "INVESTIGATING",
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "notes": []
        }

        self.incidents[incident_id] = incident

        self.counter += 1

        return incident

    def add_note(
        self,
        incident_id,
        note
    ):
        """
        Add investigation note.
        """

        if incident_id in self.incidents:
            self.incidents[incident_id]["notes"].append(note)

    def escalate_incident(
        self,
        incident_id
    ):
        """
        Escalate investigation.
        """

        if incident_id in self.incidents:
            self.incidents[incident_id]["status"] = "ESCALATED"

    def resolve_incident(
        self,
        incident_id
    ):
        """
        Mark investigation resolved.
        """

        if incident_id in self.incidents:
            self.incidents[incident_id]["status"] = "RESOLVED"

    def get_incident(
        self,
        incident_id
    ):
        """
        Return incident details.
        """

        return self.incidents.get(
            incident_id,
            None
        )

    def get_all_incidents(self):
        """
        Return all investigations.
        """

        return self.incidents

    def get_incident_count(self):
        """
        Return total investigations.
        """

        return len(self.incidents)