# Generated by Django 4.1.4 on 2023-01-30 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_alter_person_phone_number_alter_review_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 19, 50, 45, 810014, tzinfo=datetime.timezone.utc)),
        ),
    ]
