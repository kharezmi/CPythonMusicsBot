# Generated by Django 3.2.6 on 2021-08-20 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0009_auto_20210820_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='status',
        ),
    ]
