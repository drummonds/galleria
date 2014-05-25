from django.conf.urls import patterns, url
from artists.views import ArtistList, ArtistCreate, ArtistDetail, ArtistUpdate, ArtistDelete

# The leading / is in the top level pattern which might be like:
#    url(r'^things/', include('yourapp.urls')),

urlpatterns = patterns(
    '',
    url(r'^new/$', ArtistCreate.as_view(), name='artist_create'),
    url(r'^(?P<pk>\d+)/$', ArtistDetail.as_view(), name='artist_detail'),
    url(r'^(?P<pk>\d+)/update/$', ArtistUpdate.as_view(), name='artist_update'),
    url(r'^(?P<pk>\d+)/delete/$', ArtistDelete.as_view(), name='artist_delete'),
    url(r'^', ArtistList.as_view(), name='artist_list'),
)
