from rest_framework import serializers
from comute.models import Faq, About, AboutHeader, Partners, Terms

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('__all__')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('__all__')

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ('__all__')

class AboutHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHeader
        fields = ('__all__')

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ('__all__')