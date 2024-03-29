from django.db.models import Q
from django.utils import timezone
from rest_framework.filters import BaseFilterBackend


class RidesListFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        city_from = int(request.query_params.get('city_from', 0))
        if city_from:
            queryset = queryset.filter(city_from=city_from)

        place_from = int(request.query_params.get('place_from', 0))
        if place_from:
            queryset = queryset.filter(place_from=place_from)

        city_to = int(request.query_params.get('city_to', 0))
        if city_to:
            queryset = queryset.filter(
                Q(city_to=city_to) | Q(stops__city=city_to))

        place_to = int(request.query_params.get('place_to', 0))
        if place_to:
            queryset = queryset.filter(
                Q(place_to=place_to) | Q(stops__place=place_to))

        date_time_from = request.query_params.get('date_time_from', '')
        if date_time_from:
            queryset = queryset.filter(date_time__gte=date_time_from)

        date_time_to = request.query_params.get('date_time_to', '')
        if date_time_to:
            queryset = queryset.filter(date_time__lte=date_time_to)

        return queryset


class MyRidesFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        past = bool(request.query_params.get('past', 0))
        if past:
            queryset = queryset.filter(
                date_time__lt=timezone.now())

        return queryset


class RequestsListFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        city_from = int(request.query_params.get('city_from', 0))
        if city_from:
            queryset = queryset.filter(city_from=city_from)

        place_from = int(request.query_params.get('place_from', 0))
        if place_from:
            queryset = queryset.filter(place_from=place_from)

        city_to = int(request.query_params.get('city_to', 0))
        if city_to:
            queryset = queryset.filter(city_to=city_to)

        place_to = int(request.query_params.get('place_to', 0))
        if place_to:
            queryset = queryset.filter(place_to=place_to)

        date_time_from = request.query_params.get('date_time_from', '')
        if date_time_from:
            queryset = queryset.filter(date_time__gte=date_time_from)

        date_time_to = request.query_params.get('date_time_to', '')
        if date_time_to:
            queryset = queryset.filter(date_time__lte=date_time_to)

        return queryset


class BookingsListFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date_time_from = request.query_params.get('date_time_from', '')
        if date_time_from:
            queryset = queryset.filter(ride__date_time__gte=date_time_from)

        date_time_to = request.query_params.get('date_time_to', '')
        if date_time_to:
            queryset = queryset.filter(ride__date_time__lte=date_time_to)

        return queryset
