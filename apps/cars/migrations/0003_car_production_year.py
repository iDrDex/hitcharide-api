# Generated by Django 2.1 on 2018-10-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20181002_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='production_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
