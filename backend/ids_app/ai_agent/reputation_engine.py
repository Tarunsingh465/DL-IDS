# reputation_engine.py

"""
========================================================
PHASE 6 — ATTACKER REPUTATION ENGINE
========================================================

This module calculates dynamic attacker
reputation/risk scores.

Purpose:
✔ behavioral risk analysis
✔ attacker danger scoring
✔ AI threat prioritization
✔ SOC-style threat ranking

The reputation score helps the AI understand:
"How dangerous is this attacker?"
========================================================
"""


# ========================================================
# REPUTATION SCORE CALCULATOR
# ========================================================

def calculate_reputation(
    severity,
    attack_count,
    repeat_offender
):

    """
    Calculate attacker reputation score.

    Parameters:
    severity (str)
    attack_count (int)
    repeat_offender (bool)

    Returns:
    tuple:
    (
        reputation_score,
        reputation_level
    )
    """

    # ----------------------------------------------------
    # INITIAL SCORE
    # ----------------------------------------------------

    score = 0

    severity = severity.upper()

    # ----------------------------------------------------
    # SEVERITY-BASED SCORING
    # ----------------------------------------------------

    if severity == "LOW":
        score += 10

    elif severity == "MEDIUM":
        score += 30

    elif severity == "HIGH":
        score += 60

    elif severity == "CRITICAL":
        score += 90

    # ----------------------------------------------------
    # ATTACK COUNT SCORING
    # ----------------------------------------------------

    score += attack_count * 2

    # ----------------------------------------------------
    # REPEAT OFFENDER BONUS
    # ----------------------------------------------------

    if repeat_offender:
        score += 15

    # ----------------------------------------------------
    # SCORE LIMIT
    # ----------------------------------------------------

    if score > 100:
        score = 100

    # ----------------------------------------------------
    # REPUTATION LEVELS
    # ----------------------------------------------------

    if score <= 20:
        level = "SAFE"

    elif score <= 40:
        level = "SUSPICIOUS"

    elif score <= 70:
        level = "DANGEROUS"

    elif score <= 90:
        level = "HIGH RISK"

    else:
        level = "CRITICAL THREAT"

    # ----------------------------------------------------
    # FINAL RESULT
    # ----------------------------------------------------

    return (
        score,
        level
    )