# admin.py

from django.contrib import admin

from .models import TrafficLog


@admin.register(TrafficLog)
class TrafficLogAdmin(admin.ModelAdmin):

    """
    AI Threat Intelligence Admin
    """

    # ---------------------------
    # TABLE DISPLAY
    # ---------------------------

    list_display = (

        "id",

        "timestamp",

        "ip_address",

        "normalized_attack",

        "severity",

        "decision",

        "confidence",

        "repeat_offender"
    )

    # ---------------------------
    # FILTERS
    # ---------------------------

    list_filter = (

        "severity",

        "decision",

        "repeat_offender",

        "timestamp"
    )

    # ---------------------------
    # SEARCH
    # ---------------------------

    search_fields = (

        "ip_address",

        "original_attack",

        "normalized_attack"
    )

    # ---------------------------
    # ORDERING
    # ---------------------------

    ordering = (

        "-timestamp",
    )

    # ---------------------------
    # READONLY FIELDS
    # ---------------------------

    readonly_fields = (

        "timestamp",
    )