# Generated by Django 2.2.4 on 2020-04-29 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200429_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_activity',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
