# Generated by Django 2.0.5 on 2018-07-22 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_formcontact_timestrimp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='service',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='service.Service'),
        ),
    ]