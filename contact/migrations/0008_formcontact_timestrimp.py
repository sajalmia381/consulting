# Generated by Django 2.0.5 on 2018-07-19 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20180716_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='formcontact',
            name='timestrimp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
