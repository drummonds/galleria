from django.views.generic import TemplateView, View, FormView, RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class PublicView(TemplateView):
    template_name = 'public.html'

#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super(PublicView, self).dispatch(*args, **kwargs)

