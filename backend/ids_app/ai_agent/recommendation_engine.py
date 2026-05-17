# recommendation_engine.py

"""
Recommendation Engine

This module generates cybersecurity
recommendations based on:

- attack type
- severity
- attacker behavior
"""


def generate_recommendation(
    attack_type,
    severity,
    repeat_offender=False
):

    """
    Generate cybersecurity recommendations.

    Parameters:
    attack_type (str)
    severity (str)
    repeat_offender (bool)

    Returns:
    str
    """

    severity = severity.upper()

    # Recommendation database
    recommendations = {

        # Normal Traffic
        "BENIGN":
        (
            "Traffic appears normal. "
            "No immediate action required."
        ),

        # Reconnaissance
        "PORTSCAN":
        (
            "Monitor reconnaissance activity and "
            "consider firewall restrictions."
        ),

        # Brute Force
        "FTP_PATATOR":
        (
            "Restrict FTP access and enforce "
            "strong authentication policies."
        ),

        "SSH_PATATOR":
        (
            "Restrict SSH access and enable "
            "multi-factor authentication."
        ),

        "WEB_BRUTE_FORCE":
        (
            "Enable account lockout policies and "
            "temporarily block suspicious IPs."
        ),

        # Web Exploits
        "WEB_SQL_INJECTION":
        (
            "Inspect database queries immediately "
            "and apply web application firewall rules."
        ),

        "WEB_XSS":
        (
            "Sanitize user inputs and enable "
            "XSS protection mechanisms."
        ),

        # DDoS / DoS
        "DDOS":
        (
            "Enable rate limiting and block "
            "malicious traffic sources immediately."
        ),

        "DOS_HULK":
        (
            "Activate anti-DDoS protection and "
            "monitor abnormal traffic spikes."
        ),

        "DOS_GOLDENEYE":
        (
            "Inspect HTTP traffic patterns and "
            "apply server-side rate limiting."
        ),

        "DOS_SLOWHTTPTEST":
        (
            "Increase timeout protections and "
            "monitor slow HTTP connection abuse."
        ),

        "DOS_SLOWLORIS":
        (
            "Limit simultaneous HTTP connections "
            "and monitor resource exhaustion attempts."
        ),

        # Critical Exploits
        "HEARTBLEED":
        (
            "Patch vulnerable OpenSSL services "
            "immediately and rotate credentials."
        ),

        "INFILTRATION":
        (
            "Investigate lateral movement activity "
            "and isolate compromised systems."
        ),

        # Unknown Threats
        "UNKNOWN_ATTACK":
        (
            "Unknown suspicious activity detected. "
            "Further investigation is recommended."
        )
    }

    # Get base recommendation
    recommendation = recommendations.get(
        attack_type,
        (
            "Monitor suspicious network activity "
            "carefully and investigate anomalies."
        )
    )

    # Repeat attacker escalation
    if repeat_offender:

        recommendation += (
            " Repeat attacker detected."
            " Consider temporary IP ban."
        )

    # Critical severity escalation
    if severity == "CRITICAL":

        recommendation += (
            " Immediate SOC escalation recommended."
        )

    return recommendation
