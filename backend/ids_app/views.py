import json
import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .utils import predict
from .models import TrafficLog


# ===============================
# 🔥 MAIN PREDICTION API
# ===============================

@csrf_exempt
def predict_view(request):

    if request.method == 'POST':

        try:

            data = json.loads(request.body)

            features = data.get('features')

            # -----------------------
            # VALIDATION
            # -----------------------

            if not features or len(features) != 78:

                return JsonResponse({

                    "error":
                    "Invalid input. Expected 78 features."

                }, status=400)

            # -----------------------
            # ML PREDICTION
            # -----------------------

            result = predict(features)

            # -----------------------
            # SAVE TO DATABASE
            # -----------------------

            TrafficLog.objects.create(

                predicted_label=
                    result["predicted_label"],

                confidence=
                    result["confidence"],

                action=
                    result["action"]
            )

            return JsonResponse(result)

        except Exception as e:

            return JsonResponse({

                "error": str(e)

            }, status=500)

    return JsonResponse({

        "message": "Use POST request"

    })


# ===============================
# 🔥 RANDOM AUTO PREDICTION
# ===============================

@csrf_exempt
def generate_prediction(request):

    try:

        # Generate random 78 features
        features = [

            random.uniform(0, 1)

            for _ in range(78)
        ]

        # -----------------------
        # ML PREDICTION
        # -----------------------

        result = predict(features)

        # -----------------------
        # SAVE TO DATABASE
        # -----------------------

        TrafficLog.objects.create(

            predicted_label=
                result["predicted_label"],

            confidence=
                result["confidence"],

            action=
                result["action"]
        )

        return JsonResponse({

            "success": True,

            "result": result
        })

    except Exception as e:

        return JsonResponse({

            "success": False,

            "error": str(e)

        })


# ===============================
# 🔥 DASHBOARD VIEW
# ===============================

def dashboard(request):

    queryset = (
        TrafficLog.objects
        .order_by('-timestamp')
    )

    total = queryset.count()

    allow = (
        queryset
        .filter(action="ALLOW")
        .count()
    )

    blocked = (
        queryset
        .filter(action="BLOCK")
        .count()
    )

    monitor = (
        queryset
        .filter(action="MONITOR")
        .count()
    )

    logs = queryset[:50]

    context = {

        "logs": logs,

        "total": total,

        "allow": allow,

        "blocked": blocked,

        "monitor": monitor
    }

    return render(
        request,
        'ids_app/dashboard.html',
        context
    )


def get_logs(request):

    logs = TrafficLog.objects.order_by('-timestamp')

    data = []

    for log in logs:

        data.append({

            "id": log.id,

            "timestamp":
                log.timestamp.strftime("%H:%M:%S"),

            "attack_type":
                log.predicted_label,

            "action":
                log.action,

            "confidence":
                float(log.confidence),
        })      

    return JsonResponse({

        "logs": data,

        "total_logs": logs.count(),

        "allow_count":
            logs.filter(
                action="ALLOW"
            ).count(),

        "block_count":
            logs.filter(
                action="BLOCK"
            ).count(),

        "monitor_count":
            logs.filter(
                action="MONITOR"
            ).count()
    })


def analytics_data(request):

    logs = TrafficLog.objects.all()

    # =========================
    # ATTACK DISTRIBUTION
    # =========================

    attack_counts = {}

    for log in logs:

        label = log.predicted_label

        if label in attack_counts:

            attack_counts[label] += 1

        else:

            attack_counts[label] = 1

    # =========================
    # ACTION DISTRIBUTION
    # =========================

    action_counts = {

        "ALLOW": 0,
        "BLOCK": 0,
        "MONITOR": 0
    }

    for log in logs:

        if log.action == "ALLOW":

            action_counts["ALLOW"] += 1

        elif log.action == "BLOCK":

            action_counts["BLOCK"] += 1

        elif log.action == "MONITOR":

            action_counts["MONITOR"] += 1

    return JsonResponse({

        "attack_distribution":
            attack_counts,

        "action_distribution":
            action_counts
    })

# ===============================
# 🔥 LIVE THREAT STATUS API
# ===============================

def threat_status(request):

    latest_logs = (
        TrafficLog.objects
        .order_by('-timestamp')[:10]
    )

    status = "SECURE"

    message = "✅ System Secure"

    # ---------------------------
    # THREAT ANALYSIS
    # ---------------------------

    for log in latest_logs:

        if log.action == "BLOCK":

            status = "DANGER"

            message = "🚨 Threat Detected"

            break

        elif log.action == "MONITOR":

            status = "WARNING"

            message = "⚠ Suspicious Activity"

    return JsonResponse({

        "status": status,

        "message": message
    })
# -------------------------------
# 🔥 AUTO GENERATE PREDICTION API
# -------------------------------

def generate_prediction(request):

    # Generate random 78 features
    features = []

    for _ in range(78):

        value = round(
            random.uniform(0, 1),
            4
        )

        features.append(value)

    # ML Prediction
    result = predict(features)

    # Save to database
    TrafficLog.objects.create(

        predicted_label=
            result["predicted_label"],

        confidence=
            result["confidence"],

        action=
            result["action"]
    )

    return JsonResponse({

        "message":
            "Prediction generated",

        "result":
            result
    })
# -------------------------------
# 🔥 GENERATE RANDOM TRAFFIC
# -------------------------------

def generate_attack(request):

    # 78 random features
    features = [

        random.uniform(0, 1)

        for _ in range(78)
    ]

    # ML prediction
    result = predict(features)

    # Save in database
    TrafficLog.objects.create(

        predicted_label=
            result["predicted_label"],

        confidence=
            result["confidence"],

        action=
            result["action"]
    )

    # Return JSON
    return JsonResponse({

        "predicted_label":
            result["predicted_label"],

        "confidence":
            result["confidence"],

        "action":
            result["action"]
    })
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_log(request, log_id):

    try:

        log = TrafficLog.objects.get(id=log_id)

        log.delete()

        return JsonResponse({
            "message": "Log deleted successfully"
        })

    except TrafficLog.DoesNotExist:

        return JsonResponse({
            "error": "Log not found"
        }, status=404)