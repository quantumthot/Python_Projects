# Generated by Django 4.0.6 on 2022-08-02 09:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60)),
                ('course_number', models.IntegerField(blank=True, default='')),
                ('instructor_name', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name_plural': 'University Classes',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
