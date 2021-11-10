from rest_framework import viewsets
from mainAPI.api import serializers
from mainAPI import models

class Viewsets(viewsets.ModelViewSet):
    serializer_class = serializers.Serializer
    queryset = models.Main.objects.all()