# Generated by Django 5.0.4 on 2024-05-04 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_useraccount_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='avatar',
        ),
    ]
