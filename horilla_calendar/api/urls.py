"""
URL patterns for Horilla Calendar API
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from horilla_calendar.api.views import (
    UserCalendarPreferenceViewSet,
    UserAvailabilityViewSet,
)

router = DefaultRouter()
router.register(r"user-calendar-preferences", UserCalendarPreferenceViewSet)
router.register(r"user-availabilities", UserAvailabilityViewSet)

urlpatterns = [
    path("", include(router.urls)),
]