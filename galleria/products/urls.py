from django.conf.urls import patterns, url
from products.views import ProductList, ProductCreate, ProductDetail, ProductUpdate, ProductDelete
from products.views import OrderList, OrderCreate, OrderDetail, OrderUpdate, OrderDelete

# The leading / is in the top level pattern which might be like:
#    url(r'^things/', include('yourapp.urls')),

urlpatterns = patterns(
    '',
    url(r'^orders/new/$', OrderCreate.as_view(), name='order_create'),
    url(r'^orders/(?P<pk>\d+)/$', OrderDetail.as_view(), name='order_detail'),
    url(r'^orders/(?P<pk>\d+)/update/$', OrderUpdate.as_view(), name='order_update'),
    url(r'^orders/(?P<pk>\d+)/delete/$', OrderDelete.as_view(), name='order_delete'),
    url(r'^orders/', OrderList.as_view(), name='order_list'),
    url(r'^new/$', ProductCreate.as_view(), name='product_create'),
    url(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='product_update'),
    url(r'^(?P<pk>\d+)/delete/$', ProductDelete.as_view(), name='product_delete'),
    url(r'^', ProductList.as_view(), name='product_list'),
)
