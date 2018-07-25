# Generated by Django 2.0.5 on 2018-07-21 03:43

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('blog', '0016_auto_20180721_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(default=blog.models.tag_default, on_delete=django.db.models.deletion.SET_DEFAULT, to='category.Category')),
            ],
        ),
    ]