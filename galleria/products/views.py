from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProductForm
from .models import Product


class ProductCRUDView(object):
    model = Product
    form_class = ProductForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('product_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProductCRUDView, self).dispatch(*args, **kwargs)


class ProductList(ProductCRUDView, ListView):
    pass


class ProductCreate(ProductCRUDView, CreateView):
    pass


class ProductDetail(ProductCRUDView, DetailView):
    pass


class ProductUpdate(ProductCRUDView, UpdateView):
    pass


class ProductDelete(ProductCRUDView, DeleteView):
    pass
