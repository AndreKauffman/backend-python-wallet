# Generated by Django 3.2.9 on 2021-11-10 20:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('client_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('products_type', models.CharField(max_length=255)),
                ('products_name', models.CharField(max_length=255)),
                ('client_name', models.CharField(max_length=255)),
            ],
        ),
    ]
