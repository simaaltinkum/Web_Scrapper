from rest_framework import viewsets
from scrapperapp.models import PingResult
from scrapperapp.api.serializers import PingResultSerializer


class PingResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PingResult.objects.all().order_by("-created_at")
    serializer_class = PingResultSerializer
