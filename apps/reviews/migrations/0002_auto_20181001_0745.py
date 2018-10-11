# Generated by Django 2.1 on 2018-10-01 07:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rides', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='type',
            new_name='author_type',
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('ride', 'author', 'subject')},
        ),
    ]