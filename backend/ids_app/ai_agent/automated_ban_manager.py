# automated_ban_manager.py

"""
========================================================
PHASE 6B — AUTOMATED BAN MANAGER
========================================================

Purpose:

Manage temporary bans automatically.

Responsibilities:

- create temporary bans
- track expiration times
- remove expired bans
- maintain ban history
- support autonomous containment
- maintain ban statistics

Current Mode:
SIMULATION
"""

from datetime import datetime, timedelta


class AutomatedBanManager:

    def __init__(self):

        # ====================================================
        # ACTIVE BANS
        # ====================================================

        self.active_bans = {}

        # ====================================================
        # BAN HISTORY
        # ====================================================

        self.ban_history = []

        # ====================================================
        # STATISTICS
        # ====================================================

        self.total_bans_created = 0

        self.total_auto_unbans = 0

    # ========================================================
    # CREATE TEMP BAN
    # ========================================================

    def create_temp_ban(
        self,
        ip_address,
        duration_minutes
    ):

        expires_at = (

            datetime.now()

            +

            timedelta(
                minutes=duration_minutes
            )
        )

        self.active_bans[ip_address] = {

            "start_time":
            str(datetime.now()),

            "expires_at":
            expires_at,

            "duration_minutes":
            duration_minutes
        }

        self.total_bans_created += 1

        event = {

            "timestamp":
            str(datetime.now()),

            "action":
            "TEMP_BAN_CREATED",

            "ip_address":
            ip_address,

            "duration_minutes":
            duration_minutes
        }

        self.ban_history.append(
            event
        )

        return event

    # ========================================================
    # CLEANUP EXPIRED BANS
    # ========================================================

    def cleanup_expired_bans(self):

        current_time = datetime.now()

        expired_ips = []

        for ip, data in self.active_bans.items():

            if current_time >= data["expires_at"]:

                expired_ips.append(ip)

        for ip in expired_ips:

            del self.active_bans[ip]

            self.total_auto_unbans += 1

            self.ban_history.append({

                "timestamp":
                str(datetime.now()),

                "action":
                "AUTO_UNBAN",

                "ip_address":
                ip
            })

    # ========================================================
    # CHECK BAN STATUS
    # ========================================================

    def is_banned(
        self,
        ip_address
    ):

        self.cleanup_expired_bans()

        return (
            ip_address in self.active_bans
        )

    # ========================================================
    # GET ACTIVE BANS
    # ========================================================

    def get_active_bans(self):

        self.cleanup_expired_bans()

        return self.active_bans

    # ========================================================
    # GET HISTORY
    # ========================================================

    def get_history(self):

        return self.ban_history

    # ========================================================
    # STATISTICS
    # ========================================================

    def get_statistics(self):

        self.cleanup_expired_bans()

        return {

            "active_bans":
            len(self.active_bans),

            "total_bans_created":
            self.total_bans_created,

            "total_auto_unbans":
            self.total_auto_unbans
        }


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    from time import sleep

    manager = AutomatedBanManager()

    manager.create_temp_ban(

        ip_address="192.168.1.100",

        duration_minutes=0.05
    )

    print(
        "\nInitially:",
        manager.is_banned(
            "192.168.1.100"
        )
    )

    sleep(5)

    print(
        "\nAfter Waiting:",
        manager.is_banned(
            "192.168.1.100"
        )
    )

    print(
        "\nHistory:\n"
    )

    print(
        manager.get_history()
    )

    print(
        "\nStatistics:\n"
    )

    print(
        manager.get_statistics()
    )