# enforcement_audit_logger.py

"""
========================================================
PHASE 6B — ENFORCEMENT AUDIT LOGGER
========================================================

Purpose:
Record all autonomous enforcement actions.

Examples:

- BLOCK
- TEMP BAN
- MONITOR
- WATCHLIST

This creates:

✔ audit trails
✔ enforcement history
✔ AI accountability
✔ future SOC reporting
"""

from datetime import datetime


class EnforcementAuditLogger:

    def __init__(self):

        self.audit_logs = []

    # ====================================================
    # LOG ENFORCEMENT ACTION
    # ====================================================

    def log_action(
        self,
        ip_address,
        decision,
        severity,
        message
    ):

        log = {

            "timestamp":
            str(datetime.now()),

            "ip_address":
            ip_address,

            "decision":
            decision,

            "severity":
            severity,

            "message":
            message
        }

        self.audit_logs.append(log)

        return log

    # ====================================================
    # GET ALL LOGS
    # ====================================================

    def get_logs(self):

        return self.audit_logs

    # ====================================================
    # GET RECENT LOGS
    # ====================================================

    def get_recent_logs(
        self,
        limit=10
    ):

        return self.audit_logs[-limit:]
    
if __name__ == "__main__":

    logger = EnforcementAuditLogger()

    logger.log_action(
        ip_address="192.168.1.100",
        decision="BLOCK",
        severity="CRITICAL",
        message="Simulated block executed"
    )

    print(
        logger.get_logs()
    )