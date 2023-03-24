from rest_framework import serializers, generics
from .models import News, Category
from common.models import Comment
from django.contrib.auth.models import User
from userInformation.models import Profile


class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('fathers_name', 'quote', 'photo', 'job_title')
        depth = 1


class NewsSerializerView(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d.%m.%Y')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y')

    class Meta:
        model = News
        fields = ("__all__")
        depth = 1


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('__all__')
        depth = 1


class CategoryListView(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")
        depth = 1


class NewCommentsById(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d.%m.%Y')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y')

    class Meta:
        model = Comment
        fields = ("__all__")
        depth = 1


class AddNewCommentsById(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("__all__")
        depth = 1


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('pk', 'title', 'content', 'author', 'company', 'is_published', 'category', 'photo')


class CategoryListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='items_count', read_only=True)

    class Meta:
        model = Category
        fields = ("pk", "title", "count")
        depth = 1


class UserInformation(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        depth = 1