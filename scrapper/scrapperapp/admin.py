from django.contrib import admin
from .models import PingResult, Domain

admin.site.register(PingResult)
admin.site.register(Domain)
