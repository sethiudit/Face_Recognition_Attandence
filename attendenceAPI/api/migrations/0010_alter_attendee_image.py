# Generated by Django 4.0.4 on 2022-05-21 04:41

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_attendancelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='image',
            field=models.ImageField(default='imges/default.png', upload_to=api.models.Attendee.path_and_rename),
        ),
    ]