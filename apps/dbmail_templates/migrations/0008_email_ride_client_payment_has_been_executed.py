# Generated by Django 2.1 on 2018-09-24 05:07
from dbmail.models import MailTemplate
from django.db import migrations


def load_mail_template(apps, schema_editor):
    MailTemplate.objects.create(
        name="The payment for the ride has been executed",
        subject="{{ site_name }} | The payment for the ride {{ ride }} has been executed",
        message="""
        <p>You're receiving this email because your payment for the ride has been executed</p>
        <p><b>There is an information about the ride:<b><br>
        <b>Car:</b> {{ ride.car }}<br>
        <b>Number of sits:</b> {{ ride.number_of_seats }}<br>
        <b>Description:</b> {{ ride.description }}<br>
        </p>
        <p>
        The Cost Contribution for the ride includes<br>
        Driver reward: {{ ride.total_for_driver }} $
        Service fee: {{ fee_value }} $
        </p>
        <p>You can see the ride details <a href='{{ ride_detail }}'>here</a></p>
        <p>Thanks for using our site!</p>
        <p>The {{ site_name }} team</p>""",
        slug="ride_client_payment_executed",
        is_html=True,)


def delete_mail_template(apps, schema_editor):
    MailTemplate.objects.filter(
        slug='ride_client_payment_executed'
    ).delete()


def clean_cache(apps, schema_editor):
    from dbmail.models import MailTemplate, ApiKey

    MailTemplate.clean_cache()
    ApiKey.clean_cache()


class Migration(migrations.Migration):

    dependencies = [
        ('dbmail_templates', '0007_email_ride_client_payment_created'),
    ]

    operations = [
        migrations.RunPython(load_mail_template, delete_mail_template),
        migrations.RunPython(clean_cache, lambda apps, schema_editor: None),
    ]
