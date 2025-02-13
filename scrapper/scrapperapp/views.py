from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from scrapperapp.models import PingResult, Domain
from scrapperapp.api.serializers import PingResultSerializer, DomainSerializer
from scrapperapp.services.service import scrape_and_save


class PingResultView(APIView):
    def post(self, request):
        host = request.data.get("domain")

        if not host:
            return Response(
                {"error": "Host bilgisi gereklidir."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            results = scrape_and_save(host)
            return Response(
                {"message": "Veriler başarıyla kaydedildi.", "data": results},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request):
        queryset = PingResult.objects.all()
        serializer = PingResultSerializer(queryset, many=True)
        return Response(serializer.data)
