# Generated by Django 2.0.5 on 2018-07-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180708_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexbanner',
            name='details',
            field=models.TextField(),
        ),
    ]
