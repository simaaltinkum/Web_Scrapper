from django.db import models

class PingResult(models.Model):
    location = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    response_time = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.ip_address}"
