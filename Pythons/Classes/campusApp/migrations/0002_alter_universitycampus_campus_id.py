# Generated by Django 4.0.6 on 2022-08-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitycampus',
            name='campus_id',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
