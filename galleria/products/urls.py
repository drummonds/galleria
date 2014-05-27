from django.conf.urls import patterns, url
from products.views import ProductList, ProductCreate, ProductDetail, ProductUpdate, ProductDelete

# The leading / is in the top level pattern which might be like:
#    url(r'^things/', include('yourapp.urls')),

urlpatterns = patterns(
    '',
    url(r'^new/$', ProductCreate.as_view(), name='product_create'),
    url(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^(?P<pk>\d+)/delete/$', ProductDelete.as_view(), name='product_delete'),
    url(r'^', ProductList.as_view(), name='product_list'),
)
