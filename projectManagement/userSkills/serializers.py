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


class TestAllQuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillQuestion
        fields = ('__all__')
        depth = 3


class TestAddQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillQuestion
        fields = ('__all__')
        depth = 3


class TestAddAnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillQuestionAnswers
        fields = ('__all__')
        depth = 3


class SkillListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('__all__')
        depth = 10


class SkillAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('__all__')
        depth = 10


class ProjectPositionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPosition
        fields = ('__all__')
        depth = 10

