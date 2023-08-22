from django.views.generic import TemplateView


# Create your views here.

class PublicIndex(TemplateView):
    template_name = "index.html"
