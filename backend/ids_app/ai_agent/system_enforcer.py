# system_enforcer.py

"""
========================================================
PHASE 6B — SYSTEM ENFORCER
========================================================

Purpose:
Bridge AI decisions and defensive actions.

Current Mode:
SIMULATION MODE

No real firewall changes are performed.

The module simulates:

- ALLOW
- MONITOR
- WATCHLIST
- TEMP BAN
- BLOCK

Future upgrades:
- Windows Firewall
- PowerShell
- netsh
- iptables
- UFW
"""

from datetime import datetime

from .enforcement_audit_logger import (
    EnforcementAuditLogger
)

from .firewall_adapter import (
    FirewallAdapter
)

from .automated_ban_manager import (
    AutomatedBanManager
)


class SystemEnforcer:

    def __init__(self):

        # ====================================================
        # EXECUTION MODE
        # ====================================================

        self.execution_mode = "SIMULATION"

        # ====================================================
        # ENFORCEMENT HISTORY
        # ====================================================

        self.enforcement_history = []

        # ====================================================
        # AUDIT LOGGER
        # ====================================================

        self.audit_logger = (
            EnforcementAuditLogger()
        )

        # ====================================================
        # FIREWALL ADAPTER
        # ====================================================

        self.firewall = (
            FirewallAdapter()
        )

        # ====================================================
        # AUTOMATED BAN MANAGER
        # ====================================================

        self.ban_manager = (
            AutomatedBanManager()
        )

    # ========================================================
    # MAIN ENFORCEMENT FUNCTION
    # ========================================================

    def enforce(
        self,
        ip_address,
        decision,
        severity
    ):
        self.ban_manager.cleanup_expired_bans()

        """
        Execute AI defensive action.

        Parameters:
        ip_address (str)
        decision (str)
        severity (str)

        Returns:
        dict
        """

        # ====================================================
        # ALLOW
        # ====================================================

        if decision == "ALLOW":

            message = self.firewall.allow_ip(
                ip_address
            )

        # ====================================================
        # MONITOR
        # ====================================================

        elif decision == "MONITOR":

            message = self.firewall.monitor_ip(
                ip_address
            )

        # ====================================================
        # WATCHLIST
        # ====================================================

        elif decision == "WATCHLIST":

            message = self.firewall.monitor_ip(
                ip_address
            )

        # ====================================================
        # TEMP BAN
        # ====================================================

        elif decision == "TEMP BAN":

            self.ban_manager.create_temp_ban(
                ip_address=ip_address,
                duration_minutes=15
            )

            message = self.firewall.temp_ban_ip(
                ip_address,
                duration_minutes=15
            )

        # ====================================================
        # BLOCK
        # ====================================================

        elif decision == "BLOCK":

            message = self.firewall.block_ip(
                ip_address
            )

        # ====================================================
        # UNKNOWN ACTION
        # ====================================================

        else:

            message = (
                f"[SIMULATION] "
                f"Unknown action for {ip_address}"
            )

        # ====================================================
        # ENFORCEMENT RESULT
        # ====================================================

        result = {

            "timestamp":
            str(datetime.now()),

            "execution_mode":
            self.execution_mode,

            "ip_address":
            ip_address,

            "decision":
            decision,

            "severity":
            severity,

            "status":
            "SUCCESS",

            "message":
            message
        }

        # ====================================================
        # STORE ENFORCEMENT HISTORY
        # ====================================================

        self.enforcement_history.append(
            result
        )

        # ====================================================
        # AUDIT LOGGING
        # ====================================================

        self.audit_logger.log_action(

            ip_address=ip_address,

            decision=decision,

            severity=severity,

            message=message
        )


        return result

    # ========================================================
    # ENFORCEMENT HISTORY
    # ========================================================

    def get_enforcement_history(self):

        return self.enforcement_history

    # ========================================================
    # AUDIT LOGS
    # ========================================================

    def get_audit_logs(self):

        return (
            self.audit_logger
            .get_logs()
        )
    # ========================================================
    # ACTIVE BANS
    # ========================================================
    def get_active_bans(self):

        return (
            self.ban_manager
            .get_active_bans()
        )
    
    # ========================================================
    # BAN STATISTICS
    # ========================================================

    def get_ban_statistics(self):

        return (
            self.ban_manager
            .get_statistics()
        )

# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    enforcer = SystemEnforcer()

    result = enforcer.enforce(

        ip_address="192.168.1.100",

        decision="BLOCK",

        severity="CRITICAL"
    )

    print("\nEnforcement Result:\n")

    print(result)

    print("\nAudit Logs:\n")

    print(
        enforcer.get_audit_logs()
    )