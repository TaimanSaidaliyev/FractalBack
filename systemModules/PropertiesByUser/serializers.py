from rest_framework import serializers
from systemModules.models import PropertiesByUserBool


class PropertyItemPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertiesByUserBool
        fields = ('__all__')
        depth = 2


class PropertyItemGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertiesByUserBool
        fields = ('isBool',)
        depth = 1
