from rest_framework import serializers
from mainAPI import models

class Serializer(serializers.ModelSerializer):
    class meta:
        model = models.Main
        fields = '__all__'