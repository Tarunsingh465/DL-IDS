from django.urls import path
from . import views


urlpatterns = [

    # -------------------------------
    # ML Prediction API
    # -------------------------------
    path(
        'predict/',
        views.predict_view,
        name='predict'
    ),

    # -------------------------------
    # Main Dashboard
    # -------------------------------
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # -------------------------------
    # Real-Time Logs API
    # -------------------------------
    path(
        'api/logs/',
        views.get_logs,
        name='get_logs'
    ),

    # -------------------------------
    # Analytics API
    # -------------------------------
    path(
        'api/analytics/',
        views.analytics_data,
        name='analytics_data'
    ),
    path(
        'api/threat-status/',
        views.threat_status,
        name='threat_status'
    ),
    path(
        'api/generate/',
        views.generate_prediction,
        name='generate_prediction'
        ),
    path(
        'api/generate/',
        views.generate_attack,
        name='generate_attack'
        ),
    path(
        'api/delete-log/<int:log_id>/',
        views.delete_log,
        name='delete_log'
        ),
]