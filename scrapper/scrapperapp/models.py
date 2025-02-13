from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PingResult(models.Model):
    domain = models.ForeignKey(
        Domain, on_delete=models.CASCADE, related_name="ping_results"
    )
    location = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    response_time = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.domain.name} - {self.location} - {self.ip_address}"
