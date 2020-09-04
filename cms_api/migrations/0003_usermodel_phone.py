# Generated by Django 3.1.1 on 2020-09-04 03:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_api', '0002_auto_20200904_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='phone',
            field=models.IntegerField(default=2, validators=[django.core.validators.RegexValidator(message='Length has to be exactly 10 characters', regex='^.{10}$')]),
            preserve_default=False,
        ),
    ]