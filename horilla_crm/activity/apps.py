"""App configuration for the activity module."""

from django.apps import AppConfig
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class ActivityConfig(AppConfig):
    """
    Configuration class for the Activity app in Horilla CRM.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "horilla_crm.activity"
    verbose_name = _("Activity")

    def ready(self):

        super().ready()
