from django.urls import path, include
from rest_framework.routers import DefaultRouter
from scrapperapp.views import PingResultViewSet

router = DefaultRouter()
router.register(r"ping-results", PingResultViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
