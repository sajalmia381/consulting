# Generated by Django 2.0.5 on 2018-07-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
