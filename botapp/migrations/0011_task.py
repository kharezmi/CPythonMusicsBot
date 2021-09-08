# Generated by Django 3.2.6 on 2021-08-20 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botapp', '0010_remove_users_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100, verbose_name='title')),
                ('task_description', models.TextField(max_length=500, verbose_name='description')),
                ('team_assigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botapp.users', verbose_name='Select Team')),
            ],
            options={
                'ordering': ['task_name'],
            },
        ),
    ]