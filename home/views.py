from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'modelo.html'

class appView(TemplateView):
    template_name = 'index.html'