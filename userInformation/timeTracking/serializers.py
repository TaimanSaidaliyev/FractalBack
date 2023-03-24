from rest_framework import serializers
from userInformation.models import StartDay, TimeTrackingProperties


class TimeTrackingListSerializer(serializers.ModelSerializer):
    userPhoto = serializers.ImageField(source='user.profile.photo', read_only=True)
    jobTitle = serializers.CharField(source='user.profile.job_title', read_only=True)

    class Meta:
        model = StartDay
        fields = ('__all__')
        depth = 3


class TimeTrackingPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTrackingProperties
        fields = ('__all__')