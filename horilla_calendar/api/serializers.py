"""
Serializers for Horilla Calendar models
"""
from rest_framework import serializers
from horilla_calendar.models import UserCalendarPreference, UserAvailability
from horilla_core.api.serializers import HorillaUserSerializer


class UserCalendarPreferenceSerializer(serializers.ModelSerializer):
    """Serializer for UserCalendarPreference model"""

    user_details = HorillaUserSerializer(source="user", read_only=True)

    class Meta:
        model = UserCalendarPreference
        fields = "__all__"


class UserAvailabilitySerializer(serializers.ModelSerializer):
    """Serializer for UserAvailability model"""

    user_details = HorillaUserSerializer(source="user", read_only=True)

    class Meta:
        model = UserAvailability
        fields = "__all__"