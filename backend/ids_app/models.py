from django.db import models


class TrafficLog(models.Model):

    ACTION_CHOICES = [
        ("ALLOW", "Allow"),
        ("BLOCK", "Block"),
        ("MONITOR", "Monitor"),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)

    predicted_label = models.CharField(max_length=100)

    confidence = models.FloatField()

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    # 🔥 Optional (future use)
    source_ip = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.predicted_label} - {self.action} ({self.confidence})"