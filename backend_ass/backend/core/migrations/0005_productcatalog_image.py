# Generated by Django 3.0.7 on 2020-07-06 07:10

import backend.core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_productcatalog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcatalog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=backend.core.models.ProductCatalog.upload_dir),
        ),
    ]