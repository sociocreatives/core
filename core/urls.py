from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comute.urls', namespace='comute')),
    path('api/', include('comute_api.urls', namespace='comute_api')),
]
