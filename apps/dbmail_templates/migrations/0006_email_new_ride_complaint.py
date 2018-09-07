# Generated by Django 2.1 on 2018-09-07 14:46
from dbmail.models import MailTemplate
from django.db import migrations


def load_mail_template(apps, schema_editor):
    MailTemplate.objects.create(
        name="The ride has the new complaint",
        subject="The {{ complaint.ride }} has the new complaint",
        message="""
        <p>Complaint body:</p>
        <p>{{ complaint.description }}</p>
        <p><b>There is an information about the ride:<b><br>
        <b>Car:</b> {{ complaint.ride.car }}<br>
        <b>Number of sits:</b> {{ complaint.ride.number_of_sits }}<br>
        <b>Description:</b> {{ complaint.ride.description }}<br
        </p>,
        """,
            slug="new_ride_complaint",
        is_html=True,)


def clean_cache(apps, schema_editor):
    from dbmail.models import MailTemplate, ApiKey

    MailTemplate.clean_cache()
    ApiKey.clean_cache()


class Migration(migrations.Migration):

    dependencies = [
        ('dbmail_templates', '0005_email_ride_has_been_edited'),
    ]

    operations = [
        migrations.RunPython(load_mail_template),
        migrations.RunPython(clean_cache),
    ]
