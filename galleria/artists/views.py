from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from artists.forms import ArtistForm
from artists.models import Artist

class ArtistCRUDView(object):
    model = Artist
    form_class = ArtistForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('artist_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ArtistCRUDView, self).dispatch(*args, **kwargs)


class ArtistList(ArtistCRUDView, ListView):
    pass


class ArtistCreate(ArtistCRUDView, CreateView):
    pass


class ArtistDetail(ArtistCRUDView, DetailView):
    pass


class ArtistUpdate(ArtistCRUDView, UpdateView):
    pass


class ArtistDelete(ArtistCRUDView, DeleteView):
    pass

