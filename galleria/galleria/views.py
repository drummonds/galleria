from django.views.generic import TemplateView, View, FormView, RedirectView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class PublicView(TemplateView):
    template_name = 'public.html'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            url = reverse('contact_list')
            return(redirect(url))
        else:
            return(super(PublicView, self).dispatch(*args, **kwargs))

