from rest_framework import serializers
from common.models import Comment


class CommentsByRecordId(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d.%m.%Y')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y')
    author_photo = serializers.ImageField(source='author.profile.photo', read_only=True)

    class Meta:
        model = Comment
        fields = ("__all__")
        depth = 3


class AddUpdateCommentsById(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("__all__")
        depth = 3