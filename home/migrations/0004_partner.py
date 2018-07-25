# Generated by Django 2.0.5 on 2018-07-08 15:21

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180708_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to=home.models.get_partner_image_name)),
            ],
        ),
    ]
