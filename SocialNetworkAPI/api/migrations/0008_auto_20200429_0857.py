# Generated by Django 2.2.4 on 2020-04-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200429_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
