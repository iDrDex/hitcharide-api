import logging
from decimal import Decimal
from django.urls import reverse
from paypalrestsdk import Payment, Payout, ResourceNotFound


logger = logging.getLogger()


def inform_all_subscribers(ride):
    ride.stops.all().values_list('city_id').exclude()

def ride_booking_paypal_payment(request, ride_booking):
    ride_total = ride_booking.ride.price_with_fee * ride_booking.seats_count
    payment = Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url":
                request.build_absolute_uri(
                    reverse('ridebooking-paypal-payment-execute',
                            kwargs={'pk': ride_booking.pk})),
            "cancel_url": "http://localhost:3000/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "ride_booking",
                    "sku": "{0}".format(ride_booking.pk),
                    "price": '{0:.2f}'.format(ride_total),
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": '{0:.2f}'.format(ride_total),
                "currency": "USD"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        logger.error(payment.links)
        approval_link = [
            link['href'] for link in payment.links
            if link['rel'] == 'approval_url'][0]
        logger.error(approval_link)
        ride_booking.paypal_payment_id = payment.id
        ride_booking.paypal_approval_link = approval_link
        ride_booking.save()
    else:
        logger.error(payment.error)


def ride_booking_paypal_payout(ride_booking):
    payout = Payout({
        "sender_batch_header": {
            "sender_batch_id": "ride_booking_{0}".format(ride_booking.pk),
            "email_subject": "You have a payment"
        },
        "items": [
            {
                "recipient_type": "EMAIL",
                "amount": {
                    "value": float(ride_booking.ride.price),
                    "currency": "USD"
                },
                "receiver": ride_booking.ride.car.owner.paypal_account,
                "note": "Thank you.",
                "sender_item_id": "ride_booking_{0}".format(ride_booking.pk)
            }
        ]
    })

    if payout.create():
        # TODO: We need to send email to driver
        # TODO: Change RideBooking status
        print("payout[%s] created successfully" %
              (payout.batch_header.payout_batch_id))
    else:
        print(payout.error)
