# Generated by Django 2.0.5 on 2018-07-21 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_blog_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildTag',
        ),
    ]