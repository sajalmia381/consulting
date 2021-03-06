# Generated by Django 2.0.5 on 2018-07-13 09:53

import about.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20180710_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=about.models.get_about_image_name)),
                ('image_2', models.ImageField(blank=True, upload_to=about.models.get_about_image_name)),
                ('title', models.CharField(max_length=400)),
                ('details', models.TextField()),
            ],
        ),
    ]
