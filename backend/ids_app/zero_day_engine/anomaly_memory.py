"""
========================================================
PHASE 7 — ANOMALY MEMORY ENGINE
========================================================

Stores anomaly history and behavioral records.

Purpose:
- Track anomaly occurrences
- Detect repeated anomalies
- Maintain anomaly timelines
- Support threat hunting
"""

from datetime import datetime


class AnomalyMemory:

    def __init__(self):
        """
        Central anomaly storage.

        Structure:

        {
            "192.168.1.10": {
                "anomaly_count": 3,
                "scores": [0.72, 0.81, 0.91],
                "first_seen": "...",
                "last_seen": "...",
                "categories": ["ANOMALY", "HIGH_ANOMALY"]
            }
        }
        """
        self.memory = {}

    def record_anomaly(self, ip_address, score, category):
        """
        Store a newly detected anomaly.
        """

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        if ip_address not in self.memory:

            self.memory[ip_address] = {
                "anomaly_count": 0,
                "scores": [],
                "first_seen": current_time,
                "last_seen": current_time,
                "categories": []
            }

        self.memory[ip_address]["anomaly_count"] += 1
        self.memory[ip_address]["scores"].append(score)
        self.memory[ip_address]["last_seen"] = current_time

        if category not in self.memory[ip_address]["categories"]:
            self.memory[ip_address]["categories"].append(category)

        return self.memory[ip_address]

    def get_anomaly_profile(self, ip_address):
        """
        Return anomaly history for an IP.
        """

        return self.memory.get(ip_address, None)

    def get_anomaly_count(self, ip_address):
        """
        Return total anomaly count.
        """

        profile = self.memory.get(ip_address)

        if not profile:
            return 0

        return profile["anomaly_count"]

    def is_repeat_anomaly(self, ip_address):
        """
        Check whether anomaly is repeated.
        """

        return self.get_anomaly_count(ip_address) > 1

    def get_all_anomalies(self):
        """
        Return complete anomaly memory.
        """

        return self.memory