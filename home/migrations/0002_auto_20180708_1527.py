# Generated by Django 2.0.5 on 2018-07-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexbanner',
            name='details',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='indexbanner',
            name='title',
            field=models.CharField(max_length=45),
        ),
    ]
