from rest_framework import generics
from comute.models import Faq, Partners, About, AboutHeader, Terms
from .serializers import FaqSerializer, AboutSerializer, AboutHeaderSerializer, PartnersSerializer, TermsSerializer
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly


class FaqList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class FaqDetail(generics.RetrieveDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class AboutList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutHeaderList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = AboutHeader.objects.all()
    serializer_class = AboutHeaderSerializer

class PartnersList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class TermsList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Terms.objects.all()
    serializer_class = PartnersSerializer