from django.views.generic import TemplateView


class VersionInfotemplateView(TemplateView):
    template_name = "version_info/info.html"
