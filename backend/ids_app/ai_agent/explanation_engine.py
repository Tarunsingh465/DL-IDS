# explanation_engine.py

"""
Threat Explanation Engine

This module explains cybersecurity attacks
like a SOC analyst.

It provides:
- attack meaning
- attacker behavior
- cybersecurity context
"""


def generate_explanation(attack_type):

    """
    Generate cybersecurity explanation.

    Parameters:
    attack_type (str)

    Returns:
    str
    """

    # Explanation database
    explanations = {

        # Normal Traffic
        "BENIGN":
        (
            "Normal network traffic with no "
            "malicious behavior detected."
        ),

        # Reconnaissance
        "PORTSCAN":
        (
            "PortScan indicates reconnaissance "
            "activity where attackers scan open "
            "ports to identify vulnerable services."
        ),

        # Brute Force
        "FTP_PATATOR":
        (
            "FTP-Patator represents repeated "
            "FTP login attempts targeting "
            "credential compromise."
        ),

        "SSH_PATATOR":
        (
            "SSH-Patator indicates repeated "
            "SSH authentication attacks used "
            "to compromise remote systems."
        ),

        "WEB_BRUTE_FORCE":
        (
            "Web brute force attacks attempt "
            "to gain unauthorized access by "
            "guessing credentials repeatedly."
        ),

        # Web Exploits
        "WEB_SQL_INJECTION":
        (
            "SQL Injection attacks attempt "
            "to manipulate backend databases "
            "through malicious SQL queries."
        ),

        "WEB_XSS":
        (
            "Cross-Site Scripting (XSS) attacks "
            "inject malicious scripts into web "
            "applications targeting users."
        ),

        # DDoS / DoS
        "DDOS":
        (
            "Distributed Denial of Service "
            "(DDoS) attacks overwhelm systems "
            "with massive traffic to disrupt "
            "services and availability."
        ),

        "DOS_HULK":
        (
            "DoS Hulk generates extremely high "
            "HTTP traffic to exhaust server "
            "resources and availability."
        ),

        "DOS_GOLDENEYE":
        (
            "DoS GoldenEye aggressively targets "
            "web servers using repeated HTTP "
            "requests to cause disruption."
        ),

        "DOS_SLOWHTTPTEST":
        (
            "DoS SlowHTTPTest abuses slow HTTP "
            "connections to gradually consume "
            "server resources over time."
        ),

        "DOS_SLOWLORIS":
        (
            "Slowloris attacks maintain many "
            "partial HTTP connections to keep "
            "server resources occupied."
        ),

        # Critical Exploits
        "HEARTBLEED":
        (
            "Heartbleed exploits a critical "
            "OpenSSL vulnerability capable of "
            "leaking sensitive memory contents."
        ),

        "INFILTRATION":
        (
            "Infiltration attacks indicate "
            "unauthorized penetration and possible "
            "lateral movement inside the network."
        ),

        # Unknown Threats
        "UNKNOWN_ATTACK":
        (
            "Unknown suspicious activity detected. "
            "Further investigation is recommended."
        )
    }

    # Return explanation
    return explanations.get(
        attack_type,
        (
            "Suspicious network behavior detected. "
            "Further investigation is recommended."
        )
    )
