# attack_normalizer.py

"""
Attack Name Normalizer

This module converts raw dataset attack labels
into standardized internal AI attack keys.
"""


def normalize_attack_name(attack_type):

    """
    Normalize attack labels.

    Parameters:
    attack_type (str)

    Returns:
    str
    """

    # Safety handling
    if not attack_type:
        return "UNKNOWN_ATTACK"

    # Remove extra spaces
    attack_type = attack_type.strip()

    # Mapping table
    attack_map = {

        # Normal Traffic
        "BENIGN":
        "BENIGN",

        # DDoS
        "DDoS":
        "DDOS",

        # DoS Attacks
        "DoS GoldenEye":
        "DOS_GOLDENEYE",

        "DoS Hulk":
        "DOS_HULK",

        "DoS Slowhttptest":
        "DOS_SLOWHTTPTEST",

        "DoS slowloris":
        "DOS_SLOWLORIS",

        # Brute Force
        "FTP-Patator":
        "FTP_PATATOR",

        "SSH-Patator":
        "SSH_PATATOR",

        # Web Attacks
        "Web Attack - Brute Force":
        "WEB_BRUTE_FORCE",

        "Web Attack - Sql Injection":
        "WEB_SQL_INJECTION",

        "Web Attack - XSS":
        "WEB_XSS",

        # Critical Exploits
        "Heartbleed":
        "HEARTBLEED",

        "Infiltration":
        "INFILTRATION"
    }

    # Already normalized values
    normalized_values = set(
        attack_map.values()
    )

    # Prevent double normalization
    if attack_type in normalized_values:
        return attack_type

    # Return normalized attack
    return attack_map.get(
        attack_type,
        "UNKNOWN_ATTACK"
    )
