from rest_framework import viewsets
from scrapperapp.models import PingResult
from scrapperapp.serializer import PingResultSerializer

class PingResultViewSet(viewsets.ReadOnlyModelViewSet):  # ReadOnlyModelViewSet ile sadece GET isteklerini açıyoruz
    queryset = PingResult.objects.all().order_by('-created_at')
    serializer_class = PingResultSerializer
