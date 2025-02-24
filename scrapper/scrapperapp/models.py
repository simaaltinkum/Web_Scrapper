from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PingResult(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    data = models.JSONField(default=list)  # Verileri düz bir liste olarak saklıyoruz

    def __str__(self):
        return f"{self.domain.name} - {self.data}"