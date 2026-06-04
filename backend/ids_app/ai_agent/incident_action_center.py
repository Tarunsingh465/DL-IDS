# incident_action_center.py

"""
========================================================
PHASE 6B — INCIDENT ACTION CENTER
========================================================

Purpose:
Centralized Incident Management System

Tracks:

- Incident creation
- Incident escalation
- Incident resolution
- Incident history
- Incident lifecycle

Acts like a mini SOC incident tracker.
"""

from datetime import datetime


class IncidentActionCenter:

    def __init__(self):

        self.incidents = {}

        self.incident_counter = 1

    # ====================================================
    # CREATE INCIDENT
    # ====================================================

    def create_incident(
        self,
        ip_address,
        attack_type,
        severity,
        decision
    ):

        incident_id = (
            f"INC-{self.incident_counter:05d}"
        )

        self.incident_counter += 1

        incident = {

            "incident_id":
            incident_id,

            "ip_address":
            ip_address,

            "attack_type":
            attack_type,

            "severity":
            severity,

            "decision":
            decision,

            "status":
            "OPEN",

            "created_at":
            str(datetime.now()),

            "updated_at":
            str(datetime.now()),

            "timeline": [
                {
                    "event":
                    "INCIDENT_CREATED",

                    "timestamp":
                    str(datetime.now())
                }
            ]
        }

        self.incidents[
            incident_id
        ] = incident

        return incident

    # ====================================================
    # ESCALATE INCIDENT
    # ====================================================

    def escalate_incident(
        self,
        incident_id
    ):

        if incident_id not in self.incidents:
            return None

        incident = self.incidents[
            incident_id
        ]

        incident["status"] = "ESCALATED"

        incident["updated_at"] = (
            str(datetime.now())
        )

        incident["timeline"].append({

            "event":
            "INCIDENT_ESCALATED",

            "timestamp":
            str(datetime.now())
        })

        return incident

    # ====================================================
    # RESOLVE INCIDENT
    # ====================================================

    def resolve_incident(
        self,
        incident_id
    ):

        if incident_id not in self.incidents:
            return None

        incident = self.incidents[
            incident_id
        ]

        incident["status"] = "RESOLVED"

        incident["updated_at"] = (
            str(datetime.now())
        )

        incident["timeline"].append({

            "event":
            "INCIDENT_RESOLVED",

            "timestamp":
            str(datetime.now())
        })

        return incident

    # ====================================================
    # GET INCIDENT
    # ====================================================

    def get_incident(
        self,
        incident_id
    ):

        return self.incidents.get(
            incident_id
        )

    # ====================================================
    # GET ALL INCIDENTS
    # ====================================================

    def get_all_incidents(self):

        return self.incidents

    # ====================================================
    # GET OPEN INCIDENTS
    # ====================================================

    def get_open_incidents(self):

        return {

            k: v

            for k, v

            in self.incidents.items()

            if v["status"] == "OPEN"
        }

    # ====================================================
    # GET STATISTICS
    # ====================================================

    def get_statistics(self):

        total = len(
            self.incidents
        )

        open_count = len([
            i
            for i
            in self.incidents.values()
            if i["status"] == "OPEN"
        ])

        escalated_count = len([
            i
            for i
            in self.incidents.values()
            if i["status"] == "ESCALATED"
        ])

        resolved_count = len([
            i
            for i
            in self.incidents.values()
            if i["status"] == "RESOLVED"
        ])

        return {

            "total_incidents":
            total,

            "open_incidents":
            open_count,

            "escalated_incidents":
            escalated_count,

            "resolved_incidents":
            resolved_count
        }


# ========================================================
# TEST
# ========================================================

if __name__ == "__main__":

    center = IncidentActionCenter()

    incident = center.create_incident(

        ip_address="192.168.1.100",

        attack_type="DDOS",

        severity="CRITICAL",

        decision="BLOCK"
    )

    print("\nCreated:\n")

    print(incident)

    center.escalate_incident(
        incident["incident_id"]
    )

    center.resolve_incident(
        incident["incident_id"]
    )

    print("\nStatistics:\n")

    print(
        center.get_statistics()
    )