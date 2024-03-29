import datetime
from django.utils import timezone
from factory import DjangoModelFactory, fuzzy, SubFactory, Sequence, \
    post_generation

from apps.cars.factories import CarFactory
from apps.places.factories import CityFactory
from apps.accounts.factories import UserFactory
from .models import Ride, RideBooking, RideStop, RideComplaint, \
    RideComplaintStatus, RideRequest


class RideFactory(DjangoModelFactory):
    car = SubFactory(CarFactory)
    city_from = SubFactory(CityFactory)
    city_to = SubFactory(CityFactory)
    number_of_seats = fuzzy.FuzzyInteger(low=2, high=7)
    price = fuzzy.FuzzyInteger(low=2, high=100)
    date_time = fuzzy.FuzzyDateTime(
        start_dt=timezone.now() + datetime.timedelta(days=1),
        end_dt=timezone.now() + datetime.timedelta(days=10))
    description = fuzzy.FuzzyText()

    class Meta:
        model = Ride

    @post_generation
    def stops_cities(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for i, city in enumerate(extracted):
                RideStopFactory.create(
                    city=city,
                    ride=self,
                    order=i
                )


class RideStopFactory(DjangoModelFactory):
    ride = SubFactory(RideFactory)
    city = SubFactory(CityFactory)
    order = Sequence(lambda n: n)

    class Meta:
        model = RideStop


class RideBookingFactory(DjangoModelFactory):
    ride = SubFactory(RideFactory)
    client = SubFactory(UserFactory)

    class Meta:
        model = RideBooking


class RideComplaintFactory(DjangoModelFactory):
    ride = SubFactory(RideFactory)
    user = SubFactory(UserFactory)
    status = RideComplaintStatus.NEW
    description = fuzzy.FuzzyText()

    class Meta:
        model = RideComplaint


class RideRequestFactory(DjangoModelFactory):
    author = SubFactory(UserFactory)
    city_from = SubFactory(CityFactory)
    city_to = SubFactory(CityFactory)
    date_time = fuzzy.FuzzyDateTime(start_dt=timezone.now().replace(year=2003))

    class Meta:
        model = RideRequest
