# Generated by Django 4.1.4 on 2023-01-30 19:51

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=15)),
                ('patronymic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContractInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_lastname', models.CharField(max_length=30)),
                ('person_firstname', models.CharField(max_length=15)),
                ('contract_num', models.CharField(max_length=10)),
                ('person_chat_id', models.IntegerField()),
                ('person_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('post_index', models.CharField(max_length=5)),
                ('street_type', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=40)),
                ('house_number', models.CharField(max_length=4)),
                ('flat_number', models.CharField(max_length=4)),
                ('doctor_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.doctorchat')),
            ],
        ),
    ]
