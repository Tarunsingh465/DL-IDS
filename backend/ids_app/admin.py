from django.contrib import admin
from .models import TrafficLog


@admin.register(TrafficLog)
class TrafficLogAdmin(admin.ModelAdmin):
    list_display = ('predicted_label', 'confidence', 'action', 'timestamp')