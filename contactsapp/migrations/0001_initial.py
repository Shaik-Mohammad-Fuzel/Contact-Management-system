# Generated by Django 5.1.7 on 2025-03-18 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('slno', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]{1,50}$', 'Enter a valid first name')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]{1,50}$', 'Enter a valid last name')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[6-9]\\d{9}$', 'Enter a valid 10-digit phone number')])),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
            ],
        ),
    ]
