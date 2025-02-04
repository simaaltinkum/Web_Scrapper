from rest_framework import serializers
from .models import PingResult

class PingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingResult
        fields = '__all__'
