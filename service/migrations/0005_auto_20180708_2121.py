# Generated by Django 2.0.5 on 2018-07-08 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_service_icon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('name',)},
        ),
    ]
