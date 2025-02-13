from rest_framework import serializers
from scrapperapp.models import PingResult, Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "name", "created_at"]


class PingResultSerializer(serializers.ModelSerializer):
    domain = DomainSerializer(read_only=True)

    class Meta:
        model = PingResult
        fields = [
            "id",
            "domain",
            "location",
            "ip_address",
            "status",
            "response_time",
            "created_at",
        ]
