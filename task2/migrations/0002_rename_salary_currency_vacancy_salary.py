# Generated by Django 5.0.3 on 2024-03-18 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='salary_currency',
            new_name='salary',
        ),
    ]
