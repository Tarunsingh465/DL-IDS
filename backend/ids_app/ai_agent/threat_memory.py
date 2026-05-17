# threat_memory.py

"""
Threat Memory System

This module stores attacker behavior history.

The AI agent remembers:
- source IPs
- attack counts
- attack history
- repeated offenders
"""

from datetime import datetime


# -------------------------------
# GLOBAL ATTACKER MEMORY
# -------------------------------

attacker_memory = {}

# Maximum stored attack history
MAX_HISTORY = 20


# -------------------------------
# UPDATE ATTACKER MEMORY
# -------------------------------

def update_attacker_memory(
    ip_address,
    attack_type
):

    """
    Update attacker history.

    Parameters:
    ip_address (str)
    attack_type (str)

    Returns:
    dict
    """

    current_time = datetime.now().isoformat()

    # New attacker
    if ip_address not in attacker_memory:

        attacker_memory[ip_address] = {

            "attack_count":
            1,

            "attack_types":
            [attack_type],

            "unique_attacks":
            list(set([attack_type])),

            "first_seen":
            current_time,

            "last_seen":
            current_time
        }

    # Existing attacker
    else:

        attacker = attacker_memory[ip_address]

        # Increase attack count
        attacker["attack_count"] += 1

        # Store attack history
        attacker["attack_types"].append(
            attack_type
        )

        # Limit memory size
        attacker["attack_types"] = attacker[
            "attack_types"
        ][-MAX_HISTORY:]

        # Update unique attacks
        attacker["unique_attacks"] = list(
            set(attacker["attack_types"])
        )

        # Update timestamp
        attacker["last_seen"] = current_time

    return attacker_memory[ip_address]


# -------------------------------
# GET ATTACKER INFO
# -------------------------------

def get_attacker_info(ip_address):

    """
    Retrieve attacker information.

    Parameters:
    ip_address (str)

    Returns:
    dict
    """

    return attacker_memory.get(
        ip_address,
        None
    )


# -------------------------------
# REPEAT OFFENDER CHECK
# -------------------------------

def is_repeat_offender(
    ip_address,
    threshold=5
):

    """
    Check if attacker crossed
    repeat attack threshold.

    Parameters:
    ip_address (str)
    threshold (int)

    Returns:
    bool
    """

    attacker = attacker_memory.get(
        ip_address
    )

    if not attacker:
        return False

    return attacker[
        "attack_count"
    ] >= threshold


# -------------------------------
# MEMORY STATISTICS
# -------------------------------

def get_memory_statistics():

    """
    Get AI memory statistics.

    Returns:
    dict
    """

    return {

        "tracked_attackers":
        len(attacker_memory),

        "repeat_offenders":
        sum(
            1 for attacker in attacker_memory.values()
            if attacker["attack_count"] >= 5
        )
    }
