# Generated by Django 2.1 on 2018-09-25 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_auto_20180924_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
