# Generated by Django 4.1.4 on 2023-02-04 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0011_alter_review_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 4, 17, 58, 35, 914601, tzinfo=datetime.timezone.utc)),
        ),
    ]