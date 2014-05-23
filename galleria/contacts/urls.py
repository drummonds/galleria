from django.conf.urls import patterns, include, url

from .views import ContactUpdate, ContactView, ContactTypeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^contact/contacts$', ContactView.as_view(), name='contact'),
    url(r'contact/contacttypess$', ContactTypeView.as_view(), name='contact_type'),
    url(r'contact/(?P<pk>\d+)/update/$', ContactUpdate, name='contact_update')
)
