# Generated by Django 2.1 on 2018-08-29 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_auto_20180828_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='first_stop',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rides.RidePoint'),
        ),
        migrations.AddField(
            model_name='ride',
            name='last_stop',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rides.RidePoint'),
        ),
    ]