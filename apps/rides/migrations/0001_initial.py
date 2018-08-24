# Generated by Django 2.1 on 2018-08-24 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('number_of_sits', models.PositiveSmallIntegerField(verbose_name='Maximum number of sits in this car')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='car_photos')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('number_of_sits', models.PositiveSmallIntegerField(verbose_name='Available number of sits during ride')),
                ('description', models.TextField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides', to='rides.Car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RideBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('created', 'Created'), ('payed', 'Payed'), ('canceled', 'Canceled'), ('succeed', 'Succeed'), ('failed', 'Failed')], default='created', max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='rides.Ride')),
            ],
        ),
        migrations.CreateModel(
            name='RidePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_per_sit', models.PositiveIntegerField()),
                ('order', models.IntegerField(default=0)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ride_stops', to='rides.Ride')),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City')),
            ],
        ),
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('city_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='places.City')),
                ('city_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='places.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ride',
            name='stops',
            field=models.ManyToManyField(related_name='rides', through='rides.RidePoint', to='places.City', verbose_name='All points of route'),
        ),
        migrations.AlterUniqueTogether(
            name='ridebooking',
            unique_together={('ride', 'client')},
        ),
    ]
