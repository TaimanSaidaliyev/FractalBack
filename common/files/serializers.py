from rest_framework import serializers
from common.models import CommonFiles
from userInformation.serializers import UserProfileOut


class CommonFilesViewSerializer(serializers.ModelSerializer):
    property = serializers.SerializerMethodField()
    user = UserProfileOut()

    class Meta:
        model = CommonFiles
        fields = ('__all__')
        depth = 1

    def get_property(self, obj):
        return obj.file_parameters
