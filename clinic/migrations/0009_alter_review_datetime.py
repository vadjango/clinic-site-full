# Generated by Django 4.1.4 on 2023-01-30 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_alter_review_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 19, 51, 54, 44070, tzinfo=datetime.timezone.utc)),
        ),
    ]
