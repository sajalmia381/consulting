# Generated by Django 2.0.5 on 2018-07-09 06:58

from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('portfolio', '0002_auto_20180709_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(default=portfolio.models.get_default_category, on_delete=django.db.models.deletion.SET_DEFAULT, to='category.Category'),
        ),
    ]