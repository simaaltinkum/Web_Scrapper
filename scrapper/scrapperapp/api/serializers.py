from rest_framework import serializers
from scrapperapp.models import PingResult, Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "name", "created_at", "type"]


class PingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingResult
        fields = ["id", "domain", "data"]

    domain = serializers.CharField(source="domain.name", read_only=True)
    data = serializers.ListField(child=serializers.CharField(), required=True)