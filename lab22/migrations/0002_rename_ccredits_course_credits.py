# Generated by Django 5.0.7 on 2024-07-21 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab22', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='ccredits',
            new_name='credits',
        ),
    ]
