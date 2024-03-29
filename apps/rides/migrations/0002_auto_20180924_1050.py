# Generated by Django 2.1 on 2018-09-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ridebooking',
            name='paypal_approval_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ridebooking',
            name='paypal_payment_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ridebooking',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('payed', 'Payed'), ('canceled', 'Canceled'), ('expired', 'Expired'), ('refunded', 'Refunded')], default='created', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='ridebooking',
            unique_together=set(),
        ),
    ]
