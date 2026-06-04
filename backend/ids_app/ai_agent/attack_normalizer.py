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

    # --------------------------------------------------
    # SAFETY HANDLING
    # --------------------------------------------------

    if not attack_type:
        return "UNKNOWN_ATTACK"

    attack_type = str(attack_type).strip()

    # --------------------------------------------------
    # ATTACK MAPPING TABLE
    # --------------------------------------------------

    attack_map = {

        # --------------------------------------------------
        # NORMAL TRAFFIC
        # --------------------------------------------------

        "BENIGN":
        "BENIGN",

        "Benign":
        "BENIGN",

        "benign":
        "BENIGN",

        # --------------------------------------------------
        # DDOS ATTACKS
        # --------------------------------------------------

        "DDoS":
        "DDOS",

        "DDOS":
        "DDOS",

        "ddos":
        "DDOS",

        # --------------------------------------------------
        # PORT SCAN
        # --------------------------------------------------

        "PortScan":
        "PORTSCAN",

        "PORTSCAN":
        "PORTSCAN",

        "portscan":
        "PORTSCAN",

        # --------------------------------------------------
        # DOS ATTACKS
        # --------------------------------------------------

        "DoS GoldenEye":
        "DOS_GOLDENEYE",

        "DOS_GOLDENEYE":
        "DOS_GOLDENEYE",

        "DoS Hulk":
        "DOS_HULK",

        "DOS_HULK":
        "DOS_HULK",

        "DoS Slowhttptest":
        "DOS_SLOWHTTPTEST",

        "DOS_SLOWHTTPTEST":
        "DOS_SLOWHTTPTEST",

        "DoS slowloris":
        "DOS_SLOWLORIS",

        "DOS_SLOWLORIS":
        "DOS_SLOWLORIS",

        # --------------------------------------------------
        # BRUTE FORCE
        # --------------------------------------------------

        "FTP-Patator":
        "FTP_PATATOR",

        "FTP_PATATOR":
        "FTP_PATATOR",

        "SSH-Patator":
        "SSH_PATATOR",

        "SSH_PATATOR":
        "SSH_PATATOR",

        # --------------------------------------------------
        # WEB ATTACKS
        # --------------------------------------------------

        "Web Attack - Brute Force":
        "WEB_BRUTE_FORCE",

        "WEB_BRUTE_FORCE":
        "WEB_BRUTE_FORCE",

        "Web Attack - Sql Injection":
        "WEB_SQL_INJECTION",

        "WEB_SQL_INJECTION":
        "WEB_SQL_INJECTION",

        "Web Attack - XSS":
        "WEB_XSS",

        "WEB_XSS":
        "WEB_XSS",

        # --------------------------------------------------
        # CRITICAL EXPLOITS
        # --------------------------------------------------

        "Heartbleed":
        "HEARTBLEED",

        "HEARTBLEED":
        "HEARTBLEED",

        "Infiltration":
        "INFILTRATION",

        "INFILTRATION":
        "INFILTRATION"
    }

    # --------------------------------------------------
    # DIRECT LOOKUP
    # --------------------------------------------------

    if attack_type in attack_map:
        return attack_map[attack_type]

    # --------------------------------------------------
    # CASE-INSENSITIVE FALLBACK
    # --------------------------------------------------

    attack_upper = attack_type.upper()

    for key, value in attack_map.items():

        if key.upper() == attack_upper:
            return value

    # --------------------------------------------------
    # UNKNOWN ATTACK
    # --------------------------------------------------

    return "UNKNOWN_ATTACK"