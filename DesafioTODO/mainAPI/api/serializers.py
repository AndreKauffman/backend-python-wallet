from rest_framework import serializers
from mainAPI import models


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Main
        fields = '__all__'