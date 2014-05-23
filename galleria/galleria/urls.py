from django.conf.urls import patterns, include, url
from .views import PublicView
from contacts.views import ContactView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', PublicView.as_view(), name='public'),
    url(r'^contact/', include('contacts.urls')),
    url(r'^dcontacts$', ContactView.as_view(), name='contact'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    
    url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'password_reset.html'}),
    url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'password_reset.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'password_reset.html'}, name='password_reset_done'),
    url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'password_reset.html'}, name='password_reset_done'),

    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
)
