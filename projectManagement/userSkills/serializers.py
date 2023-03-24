from rest_framework import serializers, generics
from projectManagement.models import *


class ProjectPositionUsersStatus(serializers.ModelSerializer):
    class Meta:
        model = ProjectPositionUsers
        fields = ('__all__')


class ProjectPositionByUserQuestions(serializers.ModelSerializer):
    class Meta:
        model = ProjectPositionUsers
        fields = ('__all__')
        depth = 10