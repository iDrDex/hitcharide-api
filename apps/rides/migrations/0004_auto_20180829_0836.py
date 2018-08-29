# Generated by Django 2.1 on 2018-08-29 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_auto_20180829_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='first_stop',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rides.RidePoint'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='last_stop',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rides.RidePoint'),
        ),
    ]