from django.contrib import admin
from django.conf.urls import patterns, include, url

from .views import ContactView,  ContactList, ContactDetail
from .views import ContactUpdate, ContactCreate, ContactDelete
from .views import  ContactTypeView, ContactTypeDetail, ContactTypeList
from .views import  ContactTypeUpdate, ContactTypeDelete, ContactTypeCreate

admin.autodiscover()

# The leading / is in the top level pattern which might be like:
#    url(r'^things/', include('yourapp.urls')),

urlpatterns = patterns(
    '',
    url(r'^', ContactList.as_view(), name='contact_list'),
    url(r'^contacts$', ContactView.as_view(), name='contact'),
    url(r'^new/$', ContactCreate.as_view(), name='contact_create'),
    url(r'^(?P<pk>\d+)/$', ContactDetail.as_view(), name='contact_detail'),
    url(r'^(?P<pk>\d+)/update/$', ContactUpdate.as_view(), name='contact_update'),
    url(r'^(?P<pk>\d+)/delete/$', ContactDelete.as_view(), name='contact_delete'),

    url(r'^type/', ContactTypeList.as_view(), name='contacttype_list'),
    url(r'contacttypess$', ContactTypeView.as_view(), name='contact_type'),
    url(r'^type/new/$', ContactTypeCreate.as_view(), name='contacttype_create'),
    url(r'^type/(?P<pk>\d+)/$', ContactTypeDetail.as_view(), name='contacttype_detail'),
    url(r'^type/(?P<pk>\d+)/update/$', ContactTypeUpdate.as_view(), name='contacttype_update'),
    url(r'^type/(?P<pk>\d+)/delete/$', ContactTypeDelete.as_view(), name='contacttype_delete'),

)

