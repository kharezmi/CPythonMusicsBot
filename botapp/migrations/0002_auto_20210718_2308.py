# Generated by Django 3.2.4 on 2021-07-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musics',
            name='from_user',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='musics',
            name='music_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='musics',
            name='music_name',
            field=models.CharField(max_length=255),
        ),
    ]
