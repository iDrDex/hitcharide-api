# Generated by Django 2.1 on 2018-11-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0007_auto_20181030_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('completed', 'Completed'), ('canceled', 'Canceled'), ('obsolete', 'Obsolete')], default='created', max_length=10),
        ),
    ]