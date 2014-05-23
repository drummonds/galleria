from django.core.urlresolvers import reverse
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from stocks.forms import StockForm
from stocks.models import Stock


class StockCRUDView(object):
    model = Stock
    form_class = StockForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('stock_list')


class StockList(StockCRUDView, ListView):
    pass


class StockCreate(StockCRUDView, CreateView):
    pass


class StockDetail(StockCRUDView, DetailView):
    pass


class StockUpdate(StockCRUDView, UpdateView):
    pass


class StockDelete(StockCRUDView, DeleteView):
    pass
