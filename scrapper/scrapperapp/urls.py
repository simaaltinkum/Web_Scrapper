from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PingResultView

"""router = DefaultRouter()
router.register(r'ping-results', PingResultViewSet, basename='ping-result')
router.register(r'domains', DomainViewSet, basename='domain')"""

urlpatterns = [
    path("post/", PingResultView.as_view(), name="post"),
    path("get/", PingResultView.as_view(), name="get"),
]
