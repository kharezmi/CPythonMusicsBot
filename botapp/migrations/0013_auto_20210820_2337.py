# Generated by Django 3.2.6 on 2021-08-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0012_auto_20210820_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmanager',
            name='type',
        ),
        migrations.AddField(
            model_name='taskmanager',
            name='types',
            field=models.CharField(choices=[('Send All Message', 'Send Message')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
