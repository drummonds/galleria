from django.conf.urls import patterns, include, url

from .views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'contact/(?P<pk>\d+)/update/$', ContactUpdate, name='contact_update')
)
