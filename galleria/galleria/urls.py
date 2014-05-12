from django.conf.urls import patterns, include, url
from views import HomeView, LoginView, LogOut

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogOut.as_view(), name='logout'),

    url(r'^admin/', include(admin.site.urls)),
)
