# Generated by Django 3.2.6 on 2021-08-20 18:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0014_rename_types_taskmanager_txt'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='taskmanager',
            managers=[
                ('task', django.db.models.manager.Manager()),
            ],
        ),
    ]