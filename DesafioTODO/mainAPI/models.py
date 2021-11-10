from django.db import models
from uuid import uuid4

class Main(models.Model):
    client_id = models.UUIDField(primary_key=True, default = uuid4, editable=False)
    products_type = models.CharField(max_length=255)
    products_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    