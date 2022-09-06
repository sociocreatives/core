from django.urls import path
from django.views.generic import TemplateView

app_name = 'comute'

urlpatterns = [
    path('', TemplateView.as_view(template_name="comute/index.html")),
]