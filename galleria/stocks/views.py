from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StockCRUDView, self).dispatch(*args, **kwargs)


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
