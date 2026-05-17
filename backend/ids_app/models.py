# models.py

from django.db import models


class TrafficLog(models.Model):

    """
    AI Threat Intelligence Log
    """

    # ---------------------------
    # AUTONOMOUS DECISION CHOICES
    # ---------------------------

    DECISION_CHOICES = [

        ("ALLOW", "Allow"),

        ("MONITOR", "Monitor"),

        ("BLOCK", "Block"),

        ("TEMP BAN", "Temporary Ban"),

        ("CRITICAL ALERT", "Critical Alert")
    ]

    # ---------------------------
    # SEVERITY LEVELS
    # ---------------------------

    SEVERITY_CHOICES = [

        ("LOW", "Low"),

        ("MEDIUM", "Medium"),

        ("HIGH", "High"),

        ("CRITICAL", "Critical")
    ]

    # ---------------------------
    # BASIC THREAT INFO
    # ---------------------------

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    ip_address = models.CharField(
        max_length=50
    )

    original_attack = models.CharField(
        max_length=100
    )

    normalized_attack = models.CharField(
        max_length=100
    )

    confidence = models.FloatField()

    # ---------------------------
    # AI INTELLIGENCE
    # ---------------------------

    severity = models.CharField(

        max_length=20,

        choices=SEVERITY_CHOICES
    )

    decision = models.CharField(

        max_length=30,

        choices=DECISION_CHOICES
    )

    repeat_offender = models.BooleanField(
        default=False
    )

    attack_count = models.IntegerField(
        default=1
    )

    # ---------------------------
    # AI ANALYSIS
    # ---------------------------

    recommendation = models.TextField()

    explanation = models.TextField()

    # ---------------------------
    # OPTIONAL FUTURE EXPANSION
    # ---------------------------

    notes = models.TextField(

        null=True,
        blank=True
    )

    # ---------------------------
    # STRING REPRESENTATION
    # ---------------------------

    def __str__(self):

        return (

            f"{self.normalized_attack}"

            f" | "

            f"{self.severity}"

            f" | "

            f"{self.decision}"
        )