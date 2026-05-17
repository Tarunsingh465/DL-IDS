# urls.py

from django.urls import path

from . import views


urlpatterns = [

    # =================================
    # DASHBOARD
    # =================================

    path(

        'dashboard/',

        views.dashboard,

        name='dashboard'
    ),

    # =================================
    # AI PREDICTION API
    # =================================

    path(

        'predict/',

        views.predict_view,

        name='predict'
    ),

    # =================================
    # AUTO TRAFFIC GENERATION
    # =================================

    path(

        'api/generate/',

        views.generate_prediction,

        name='generate_prediction'
    ),

    # =================================
    # LIVE LOGS API
    # =================================

    path(

        'api/logs/',

        views.get_logs,

        name='get_logs'
    ),

    # =================================
    # ANALYTICS API
    # =================================

    path(

        'api/analytics/',

        views.analytics_data,

        name='analytics_data'
    ),

    # =================================
    # LIVE THREAT STATUS
    # =================================

    path(

        'api/threat-status/',

        views.threat_status,

        name='threat_status'
    ),

    # =================================
    # DELETE LOG API
    # =================================

    path(

        'api/delete-log/<int:log_id>/',

        views.delete_log,

        name='delete_log'
    )
]