from django.conf.urls import patterns, url
from categories.views import CategoryList, CategoryCreate, CategoryDetail, CategoryUpdate, CategoryDelete

# The leading / is in the top level pattern which might be like:
#    url(r'^things/', include('yourapp.urls')),

urlpatterns = patterns(
    '',
    url(r'^new/$', CategoryCreate.as_view(), name='category_create'),
    url(r'^(?P<pk>\d+)/$', CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<pk>\d+)/update/$', CategoryUpdate.as_view(), name='category_update'),
    url(r'^(?P<pk>\d+)/delete/$', CategoryDelete.as_view(), name='category_delete'),
    url(r'^', CategoryList.as_view(), name='category_list'),
)
