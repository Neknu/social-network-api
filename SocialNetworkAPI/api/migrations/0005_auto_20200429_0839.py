# Generated by Django 2.2.4 on 2020-04-29 05:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_activeuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ActiveUser',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_login',
            new_name='last_activity',
        ),
    ]
