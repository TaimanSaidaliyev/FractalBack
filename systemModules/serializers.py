from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Company


class TokenSer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ("__all__")
        depth = 1


class CompanyInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('__all__')
        depth = 1

