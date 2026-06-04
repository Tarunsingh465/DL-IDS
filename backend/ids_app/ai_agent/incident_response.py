# incident_response.py

"""
========================================================
PHASE 6 — INCIDENT RESPONSE ENGINE
========================================================

This module generates autonomous
AI-driven security incident reports.

Purpose:
✔ incident documentation
✔ SOC-style reporting
✔ autonomous response summaries
✔ cyber-defense audit logs
✔ explainable security events
========================================================
"""

from datetime import datetime


# ========================================================
# INCIDENT REPORT GENERATOR
# ========================================================

def generate_incident_report(
    ip_address,
    attack_type,
    severity,
    reputation_level,
    decision,
    recommendation
):

    """
    Generate AI-driven incident report.

    Parameters:
    ip_address (str)
    attack_type (str)
    severity (str)
    reputation_level (str)
    decision (str)
    recommendation (str)

    Returns:
    dict
    """

    # ----------------------------------------------------
    # INCIDENT TIMESTAMP
    # ----------------------------------------------------

    timestamp = str(datetime.now())

    # ----------------------------------------------------
    # INCIDENT TITLE
    # ----------------------------------------------------

    title = (
        f"{severity} SECURITY INCIDENT"
    )

    # ----------------------------------------------------
    # INCIDENT SUMMARY
    # ----------------------------------------------------

    summary = (

        f"AI security agent detected "
        f"{attack_type} activity from "
        f"attacker IP {ip_address}. "

        f"The attacker was classified as "
        f"'{reputation_level}' and the "
        f"system autonomously executed "
        f"the action: {decision}."
    )

    # ----------------------------------------------------
    # RESPONSE ACTION DESCRIPTION
    # ----------------------------------------------------

    if decision == "BLOCK":

        response_action = (
            "Permanent defensive blocking "
            "was applied to contain the threat."
        )

    elif decision == "TEMP BAN":

        response_action = (
            "Temporary containment measures "
            "were activated against the attacker."
        )

    elif decision == "MONITOR":

        response_action = (
            "The attacker was placed under "
            "active monitoring."
        )

    else:

        response_action = (
            "No aggressive defensive action "
            "was required."
        )

    # ----------------------------------------------------
    # FINAL INCIDENT REPORT
    # ----------------------------------------------------

    report = {

        "timestamp":
        timestamp,

        "incident_title":
        title,

        "attacker_ip":
        ip_address,

        "attack_type":
        attack_type,

        "severity":
        severity,

        "reputation_level":
        reputation_level,

        "autonomous_decision":
        decision,

        "summary":
        summary,

        "response_action":
        response_action,

        "recommendation":
        recommendation
    }

    return report