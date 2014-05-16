from django.views.generic import TemplateView, View, FormView, RedirectView


class HomeView(TemplateView):
    template_name = 'index.html'
