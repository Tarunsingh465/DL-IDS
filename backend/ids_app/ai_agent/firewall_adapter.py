# firewall_adapter.py

"""
========================================================
PHASE 6B — FIREWALL ADAPTER
========================================================

Purpose:
Acts as the abstraction layer between
AI enforcement actions and firewall systems.

Current Mode:
SIMULATION

Future Support:

- Windows Defender Firewall
- PowerShell
- netsh
- iptables
- UFW
- Cloud Firewalls

This module prevents direct firewall
dependencies inside SystemEnforcer.
"""

from datetime import datetime


class FirewallAdapter:

    def __init__(self):

        self.mode = "SIMULATION"

        self.firewall_history = []

    # ====================================================
    # BLOCK IP
    # ====================================================

    def block_ip(self, ip_address):

        message = (
            f"[FIREWALL SIMULATION] "
            f"Blocking IP {ip_address}"
        )

        self._log_action(
            "BLOCK",
            ip_address,
            message
        )

        print(message)

        return message

    # ====================================================
    # TEMP BAN IP
    # ====================================================

    def temp_ban_ip(
        self,
        ip_address,
        duration_minutes
    ):

        message = (
            f"[FIREWALL SIMULATION] "
            f"Temporary ban for "
            f"{ip_address} "
            f"({duration_minutes} min)"
        )

        self._log_action(
            "TEMP_BAN",
            ip_address,
            message
        )

        print(message)

        return message

    # ====================================================
    # MONITOR IP
    # ====================================================

    def monitor_ip(self, ip_address):

        message = (
            f"[FIREWALL SIMULATION] "
            f"Monitoring {ip_address}"
        )

        self._log_action(
            "MONITOR",
            ip_address,
            message
        )

        print(message)

        return message

    # ====================================================
    # ALLOW IP
    # ====================================================

    def allow_ip(self, ip_address):

        message = (
            f"[FIREWALL SIMULATION] "
            f"Allowing {ip_address}"
        )

        self._log_action(
            "ALLOW",
            ip_address,
            message
        )

        print(message)

        return message

    # ====================================================
    # INTERNAL LOGGER
    # ====================================================

    def _log_action(
        self,
        action,
        ip_address,
        message
    ):

        self.firewall_history.append({

            "timestamp":
            str(datetime.now()),

            "action":
            action,

            "ip_address":
            ip_address,

            "message":
            message
        })

    # ====================================================
    # HISTORY
    # ====================================================

    def get_history(self):

        return self.firewall_history