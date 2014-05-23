from django.conf.urls import patterns, url
from stocks.views import StockList, StockCreate, StockDetail, StockUpdate, StockDelete


urlpatterns = patterns(
    '',
    url(r'^new/$', StockCreate.as_view(), name='stock_create'),
    url(r'^(?P<pk>\d+)/$', StockDetail.as_view(), name='stock_detail'),
    url(r'^(?P<pk>\d+)/update/$', StockUpdate.as_view(), name='stock_update'),
    url(r'^(?P<pk>\d+)/delete/$', StockDelete.as_view(), name='stock_delete'),
    url(r'^', StockList.as_view(), name='stock_list'),
)
