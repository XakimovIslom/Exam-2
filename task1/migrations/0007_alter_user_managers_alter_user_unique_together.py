# Generated by Django 5.0.3 on 2024-03-18 05:30

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0006_alter_user_managers_alter_user_unique_together'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('email', 'is_deleted')},
        ),
    ]