# Generated by Django 2.0.7 on 2018-07-05 12:23

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180705_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to=blog.models.get_image_name),
        ),
    ]
