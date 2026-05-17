# severity_engine.py

"""
Severity Analysis Engine

This module calculates threat severity
based on:

- attack type
- confidence score
- repeated attacker behavior

Severity Levels:
LOW
MEDIUM
HIGH
CRITICAL
"""


# -------------------------------
# SEVERITY ESCALATION HELPER
# -------------------------------

def escalate_severity(severity):

    """
    Escalate severity by one level.

    Parameters:
    severity (str)

    Returns:
    str
    """

    escalation_map = {

        "LOW":
        "MEDIUM",

        "MEDIUM":
        "HIGH",

        "HIGH":
        "CRITICAL",

        "CRITICAL":
        "CRITICAL"
    }

    return escalation_map.get(
        severity,
        "HIGH"
    )


# -------------------------------
# MAIN SEVERITY ENGINE
# -------------------------------

def calculate_severity(
    attack_type,
    confidence,
    repeat_count=0
):

    """
    Calculate threat severity.

    Parameters:
    attack_type (str)
    confidence (float)
    repeat_count (int)

    Returns:
    str
    """

    # Base severity mapping
    severity_map = {

        # Normal Traffic
        "BENIGN":
        "LOW",

        # Reconnaissance
        "PORTSCAN":
        "MEDIUM",

        # Brute Force
        "FTP_PATATOR":
        "HIGH",

        "SSH_PATATOR":
        "HIGH",

        "WEB_BRUTE_FORCE":
        "HIGH",

        # Web Exploits
        "WEB_SQL_INJECTION":
        "CRITICAL",

        "WEB_XSS":
        "HIGH",

        # DDoS / DoS
        "DDOS":
        "CRITICAL",

        "DOS_HULK":
        "CRITICAL",

        "DOS_GOLDENEYE":
        "HIGH",

        "DOS_SLOWHTTPTEST":
        "HIGH",

        "DOS_SLOWLORIS":
        "HIGH",

        # Critical Exploits
        "HEARTBLEED":
        "CRITICAL",

        "INFILTRATION":
        "CRITICAL",

        # Unknown threats
        "UNKNOWN_ATTACK":
        "HIGH"
    }

    # Get base severity
    severity = severity_map.get(
        attack_type,
        "MEDIUM"
    )

    # Confidence-based escalation
    if (
        attack_type != "BENIGN"
        and confidence >= 0.95
    ):

        severity = escalate_severity(
            severity
        )

    # Repeat attacker escalation
    if repeat_count >= 5:
        severity = escalate_severity(
            severity
        )

    return severity
