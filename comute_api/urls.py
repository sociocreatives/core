from django.urls import path
from .views import FaqList, FaqDetail, PartnersList, AboutHeaderList, AboutList, TermsList

app_name = 'comute_api'

urlpatterns = [
    path('faq/<int:pk>/', FaqDetail.as_view(), name='faqdetail'),
    path('faq/', FaqList.as_view(), name='faqlist'),
    path('about/', AboutList.as_view(), name='aboutlist'),
    path('partners/', PartnersList.as_view(), name='partnerslist'),
    path('aboutheader/', AboutHeaderList.as_view(), name='aboutheaderlist'),
    path('terms/', TermsList.as_view(), name='termslist'),
]