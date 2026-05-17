# views.py

import json
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import TrafficLog
from .utils import predict


# =====================================
# DASHBOARD VIEW
# =====================================

def dashboard(request):

    logs = (
        TrafficLog.objects
        .order_by('-timestamp')[:50]
    )

    context = {

        "logs":
        logs
    }

    return render(

        request,

        'ids_app/dashboard.html',

        context
    )


# =====================================
# MAIN AI PREDICTION API
# =====================================

@csrf_exempt
def predict_view(request):

    if request.method != "POST":

        return JsonResponse({

            "error":
            "POST request required"

        }, status=405)

    try:

        # Parse request body
        data = json.loads(
            request.body
        )

        features = data.get(
            "features"
        )

        # Validate features
        if not features:

            return JsonResponse({

                "error":
                "Features missing"

            }, status=400)

        if len(features) != 78:

            return JsonResponse({

                "error":
                "Expected 78 features"

            }, status=400)

        # AI prediction
        result = predict(
            features
        )

        # Save AI threat log
        save_traffic_log(
            result
        )

        return JsonResponse(

            result,

            safe=False
        )

    except Exception as e:

        return JsonResponse({

            "error":
            str(e)

        }, status=500)


# =====================================
# AUTO GENERATE TRAFFIC
# =====================================

@csrf_exempt
def generate_prediction(request):

    try:

        # Generate fake traffic
        features = [

            random.uniform(0, 1)

            for _ in range(78)
        ]

        # AI prediction
        result = predict(
            features
        )

        # Save log
        save_traffic_log(
            result
        )

        return JsonResponse({

            "success":
            True,

            "result":
            result
        })

    except Exception as e:

        return JsonResponse({

            "success":
            False,

            "error":
            str(e)

        })


# =====================================
# SAVE AI THREAT LOG
# =====================================

def save_traffic_log(result):

    """
    Save AI threat intelligence
    into database.
    """

    TrafficLog.objects.create(

        ip_address=
        result["ip_address"],

        original_attack=
        result["original_attack"],

        normalized_attack=
        result["normalized_attack"],

        confidence=
        result["confidence"],

        severity=
        result["severity"],

        decision=
        result["decision"],

        repeat_offender=
        result["repeat_offender"],

        attack_count=
        result["attack_count"],

        recommendation=
        result["recommendation"],

        explanation=
        result["explanation"]
    )


# =====================================
# FETCH LIVE LOGS
# =====================================

def get_logs(request):

    logs = (
        TrafficLog.objects
        .order_by('-timestamp')[:100]
    )

    data = []

    for log in logs:

        data.append({

            "id":
            log.id,

            "timestamp":
            log.timestamp.strftime(
                "%H:%M:%S"
            ),

            # --------------------------------
            # NEW AI FIELDS
            # --------------------------------

            "ip_address":
            log.ip_address,

            "attack_type":
            log.normalized_attack,

            "severity":
            log.severity,

            "decision":
            log.decision,

            "confidence":
            float(log.confidence),

            "repeat_offender":
            log.repeat_offender,

            "recommendation":
            log.recommendation,

            "explanation":
            log.explanation,

            # --------------------------------
            # BACKWARD COMPATIBILITY
            # --------------------------------

            "action":
            log.decision
        })

    queryset = TrafficLog.objects.all()

    return JsonResponse({

        "logs":
        data,

        "total_logs":
        queryset.count(),

        "allow_count":

        queryset.filter(
            decision="ALLOW"
        ).count(),

        "block_count":

        queryset.filter(
            decision="BLOCK"
        ).count(),

        "monitor_count":

        queryset.filter(
            decision="MONITOR"
        ).count()
    })


# =====================================
# ANALYTICS API
# =====================================

def analytics_data(request):

    logs = TrafficLog.objects.all()

    # -------------------------------
    # ATTACK DISTRIBUTION
    # -------------------------------

    attack_distribution = {}

    for log in logs:

        label = log.normalized_attack

        attack_distribution[label] = (

            attack_distribution.get(
                label,
                0
            ) + 1
        )

    # -------------------------------
    # DECISION DISTRIBUTION
    # -------------------------------

    decision_distribution = {

        "ALLOW": 0,

        "MONITOR": 0,

        "BLOCK": 0,

        "TEMP BAN": 0,

        "CRITICAL ALERT": 0
    }

    for log in logs:

        if log.decision in decision_distribution:

            decision_distribution[
                log.decision
            ] += 1

    return JsonResponse({

        "attack_distribution":
        attack_distribution,

        "action_distribution":
        decision_distribution
    })


# =====================================
# LIVE THREAT STATUS
# =====================================

def threat_status(request):

    latest_logs = (

        TrafficLog.objects
        .order_by('-timestamp')[:10]
    )

    status = "SECURE"

    message = "✅ System Secure"

    for log in latest_logs:

        if log.severity == "CRITICAL":

            status = "DANGER"

            message = (
                "🚨 Critical Threat Activity"
            )

            break

        elif log.severity == "HIGH":

            status = "WARNING"

            message = (
                "⚠ High Threat Activity"
            )

    return JsonResponse({

        "status":
        status,

        "message":
        message
    })


# =====================================
# DELETE LOG API
# =====================================

@csrf_exempt
def delete_log(request, log_id):

    try:

        log = TrafficLog.objects.get(
            id=log_id
        )

        log.delete()

        return JsonResponse({

            "success":
            True,

            "message":
            "Log deleted successfully"
        })

    except TrafficLog.DoesNotExist:

        return JsonResponse({

            "success":
            False,

            "error":
            "Log not found"

        }, status=404)