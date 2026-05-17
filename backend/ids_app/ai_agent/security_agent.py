# security_agent.py

"""
Autonomous AI Security Agent

This module acts as the main AI brain
for the IDS/IPS platform.

Responsibilities:
- threat analysis
- memory tracking
- severity scoring
- IPS decisions
- recommendations
- attack explanations
"""

# Import engines
from .severity_engine import (
    calculate_severity
)

from .threat_memory import (
    update_attacker_memory,
    is_repeat_offender
)

from .recommendation_engine import (
    generate_recommendation
)

from .explanation_engine import (
    generate_explanation
)

from .attack_normalizer import (
    normalize_attack_name
)


# -------------------------------
# AUTONOMOUS IPS DECISION ENGINE
# -------------------------------

def autonomous_decision(
    severity,
    repeat_offender
):

    """
    Generate autonomous IPS action.

    Parameters:
    severity (str)
    repeat_offender (bool)

    Returns:
    str
    """

    severity = severity.upper()

    # Critical threats
    if severity == "CRITICAL":

        if repeat_offender:
            return "CRITICAL ALERT"

        return "BLOCK"

    # High severity threats
    if severity == "HIGH":

        if repeat_offender:
            return "TEMP BAN"

        return "BLOCK"

    # Medium severity threats
    if severity == "MEDIUM":
        return "MONITOR"

    # Low severity threats
    return "ALLOW"


# -------------------------------
# MAIN AI ANALYSIS PIPELINE
# -------------------------------

def analyze_threat(
    ip_address,
    attack_type,
    confidence
):

    """
    Analyze detected threat.

    Parameters:
    ip_address (str)
    attack_type (str)
    confidence (float)

    Returns:
    dict
    """

    # Normalize attack label
    normalized_attack = normalize_attack_name(
        attack_type
    )

    # Update attacker memory
    attacker_info = update_attacker_memory(
        ip_address,
        normalized_attack
    )

    # Repeat offender detection
    repeat_offender = is_repeat_offender(
        ip_address
    )

    # Calculate severity
    severity = calculate_severity(
        attack_type=normalized_attack,
        confidence=confidence,
        repeat_count=attacker_info[
            "attack_count"
        ]
    )

    # Autonomous IPS decision
    decision = autonomous_decision(
        severity,
        repeat_offender
    )

    # Generate recommendation
    recommendation = generate_recommendation(
        attack_type=normalized_attack,
        severity=severity,
        repeat_offender=repeat_offender
    )

    # Generate explanation
    explanation = generate_explanation(
        normalized_attack
    )

    # Final AI intelligence response
    response = {

        "ip_address":
        ip_address,

        "original_attack":
        attack_type,

        "normalized_attack":
        normalized_attack,

        "confidence":
        round(confidence, 4),

        "severity":
        severity,

        "decision":
        decision,

        "repeat_offender":
        repeat_offender,

        "attack_count":
        attacker_info["attack_count"],

        "unique_attacks":
        attacker_info["unique_attacks"],

        "first_seen":
        attacker_info["first_seen"],

        "last_seen":
        attacker_info["last_seen"],

        "recommendation":
        recommendation,

        "explanation":
        explanation
    }

    return response