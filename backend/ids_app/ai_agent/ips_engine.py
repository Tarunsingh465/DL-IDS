# ips_engine.py

"""
========================================================
PHASE 6 — AUTONOMOUS IPS ENGINE
========================================================

This module acts as the central autonomous IPS controller.

Responsibilities:
✔ watch suspicious attackers
✔ apply temporary bans
✔ permanently block attackers
✔ escalate repeat offenders
✔ track AI defensive actions
✔ simulate autonomous cyber defense behavior
✔ manage IPS state transitions
"""

from datetime import datetime, timedelta


class IPSEngine:

    def __init__(self):

        # ====================================================
        # WATCHLIST SYSTEM
        # ====================================================

        self.watchlist_ips = {}

        # ====================================================
        # TEMP BAN SYSTEM
        # ====================================================

        self.temp_banned_ips = {}

        # ====================================================
        # PERMANENT BLOCK SYSTEM
        # ====================================================

        self.blocked_ips = {}

        # ====================================================
        # ACTION HISTORY
        # ====================================================

        self.action_history = []

    # ========================================================
    # WATCHLIST FUNCTION
    # ========================================================

    def add_to_watchlist(self, ip_address, reason):

        if ip_address in self.blocked_ips:
            return

        self.watchlist_ips[ip_address] = {
            "reason": reason,
            "timestamp": str(datetime.now())
        }

        self.log_action(
            ip_address,
            "WATCHLIST",
            f"IP added to watchlist due to {reason}"
        )

    # ========================================================
    # TEMP BAN FUNCTION
    # ========================================================

    def temp_ban_ip(
        self,
        ip_address,
        reason,
        severity,
        duration_minutes=5
    ):

        if ip_address in self.blocked_ips:
            return

        if ip_address in self.watchlist_ips:
            del self.watchlist_ips[ip_address]

        ban_until = (
            datetime.now() +
            timedelta(minutes=duration_minutes)
        )

        self.temp_banned_ips[ip_address] = {
            "reason": reason,
            "severity": severity,
            "ban_until": ban_until
        }

        self.log_action(
            ip_address,
            "TEMP_BAN",
            f"Temporary ban applied for {duration_minutes} minutes"
        )

    # ========================================================
    # PERMANENT BLOCK FUNCTION
    # ========================================================

    def block_ip(
        self,
        ip_address,
        reason,
        severity
    ):

        if ip_address in self.watchlist_ips:
            del self.watchlist_ips[ip_address]

        if ip_address in self.temp_banned_ips:
            del self.temp_banned_ips[ip_address]

        self.blocked_ips[ip_address] = {
            "reason": reason,
            "severity": severity,
            "timestamp": str(datetime.now())
        }

        self.log_action(
            ip_address,
            "BLOCK",
            "Permanent block applied"
        )

    # ========================================================
    # CLEANUP EXPIRED TEMP BANS
    # ========================================================

    def cleanup_expired_bans(self):

        current_time = datetime.now()

        expired_ips = []

        for ip, data in self.temp_banned_ips.items():

            if current_time > data["ban_until"]:
                expired_ips.append(ip)

        for ip in expired_ips:

            del self.temp_banned_ips[ip]

            self.log_action(
                ip,
                "UNBAN",
                "Temporary ban expired"
            )

    # ========================================================
    # IPS DECISION ENGINE
    # ========================================================

    def decide_ips_action(
        self,
        ip_address,
        severity,
        attack_count,
        attack_type
    ):

        """
        IPS Decision Rules

        BENIGN
            -> ALLOW

        LOW
            -> MONITOR

        MEDIUM
            -> WATCHLIST / TEMP BAN

        HIGH
            -> WATCHLIST / TEMP BAN

        CRITICAL
            -> TEMP BAN / BLOCK
        """

        # Cleanup old bans
        self.cleanup_expired_bans()

        # ====================================================
        # BENIGN TRAFFIC
        # ====================================================

        if attack_type == "BENIGN":

            # Remove stale watchlist entry
            if ip_address in self.watchlist_ips:
                del self.watchlist_ips[ip_address]

            return "ALLOW"

        # ====================================================
        # BLOCKED ATTACKERS REMAIN BLOCKED
        # ====================================================

        if ip_address in self.blocked_ips:
            return "BLOCK"

        # ====================================================
        # LOW SEVERITY
        # ====================================================

        if severity == "LOW":

            self.add_to_watchlist(
                ip_address,
                attack_type
            )

            return "MONITOR"

        # ====================================================
        # MEDIUM SEVERITY
        # ====================================================

        elif severity == "MEDIUM":

            if attack_count >= 3:

                self.temp_ban_ip(
                    ip_address,
                    attack_type,
                    severity,
                    duration_minutes=5
                )

                return "TEMP BAN"

            self.add_to_watchlist(
                ip_address,
                attack_type
            )

            return "MONITOR"

        # ====================================================
        # HIGH SEVERITY
        # ====================================================

        elif severity == "HIGH":

            if attack_count >= 3:

                self.temp_ban_ip(
                    ip_address,
                    attack_type,
                    severity,
                    duration_minutes=10
                )

                return "TEMP BAN"

            self.add_to_watchlist(
                ip_address,
                attack_type
            )

            return "MONITOR"

        # ====================================================
        # CRITICAL SEVERITY
        # ====================================================

        elif severity == "CRITICAL":

            if attack_count >= 5:

                self.block_ip(
                    ip_address,
                    attack_type,
                    severity
                )

                return "BLOCK"

            self.temp_ban_ip(
                ip_address,
                attack_type,
                severity,
                duration_minutes=15
            )

            return "TEMP BAN"

        # ====================================================
        # DEFAULT FALLBACK
        # ====================================================

        return "MONITOR"

    # ========================================================
    # ACTION LOGGER
    # ========================================================

    def log_action(
        self,
        ip_address,
        action,
        message
    ):

        log = {
            "ip_address": ip_address,
            "action": action,
            "message": message,
            "timestamp": str(datetime.now())
        }

        self.action_history.append(log)

    # ========================================================
    # STATUS GETTERS
    # ========================================================

    def get_watchlist(self):
        return self.watchlist_ips

    def get_temp_banned_ips(self):
        return self.temp_banned_ips

    def get_blocked_ips(self):
        return self.blocked_ips

    def get_action_history(self):
        return self.action_history