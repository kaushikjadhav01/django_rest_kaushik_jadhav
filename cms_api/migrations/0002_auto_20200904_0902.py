# Generated by Django 3.1.1 on 2020-09-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='phone',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]