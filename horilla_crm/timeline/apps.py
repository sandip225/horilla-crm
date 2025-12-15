""" "Configuration for the timeline app in Horilla CRM."""

from django.apps import AppConfig
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class TimelineConfig(AppConfig):
    """Configuration class for the Timeline app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "horilla_crm.timeline"
    verbose_name = _("Timeline")

    def ready(self):

        super().ready()
