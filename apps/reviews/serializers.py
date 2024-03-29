from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.accounts.serializers import UserPublicSerializer
from apps.rides.models import RideBookingStatus, RideStatus
from .models import Review, ReviewAuthorType


class ReviewSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer()

    class Meta:
        model = Review
        fields = ('pk', 'created', 'author', 'author_type',
                  'ride', 'subject', 'rating', 'comment')


class ReviewWritableSerializer(ReviewSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        ride = attrs['ride']
        if ride.date_time > timezone.now():
            raise ValidationError('Ride must be started to create the review')

        author = attrs['author']
        subject = attrs['subject']

        ride_passengers_pks = ride.payed_bookings.values_list(
            'client_id', flat=True)
        ride_driver = ride.car.owner

        if attrs['author_type'] == ReviewAuthorType.DRIVER:
            if author != ride_driver:
                raise ValidationError('Review author must be a driver '
                                      'if author_type = DRIVER')

            if subject.pk not in ride_passengers_pks:
                raise ValidationError('Review subject must be a passenger '
                                      'if author_type = DRIVER')
        else:
            if subject != ride_driver:
                raise ValidationError('Review subject must be a driver '
                                      'if author_type = PASSENGER')

            if author.pk not in ride_passengers_pks:
                raise ValidationError('Review author must be a passenger '
                                      'if author_type = PASSENGER')

        return super(ReviewWritableSerializer, self).validate(attrs)

    class Meta(ReviewSerializer.Meta):
        pass
