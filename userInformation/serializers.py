from rest_framework import serializers
from .models import Profile, Company
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active')
        depth = 1


class ProfileSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('photo', 'job_title')
        depth = 2


class UserProfileOut(serializers.ModelSerializer):
    profile = ProfileSerializerOut()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile']