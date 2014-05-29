from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView

from django_tables2   import RequestConfig, SingleTableView
from .tables import CategoryTable, ThemedCategoryTable
from .models import Category

from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import CategoryForm
from .models import Category,CategoryFilter
from galleria.filter_mixin import ListFilteredMixin


# Try out for tables2
class CategoryList(ListFilteredMixin,SingleTableView):
    table_class = ThemedCategoryTable
    queryset = Category.objects.order_by('name').all()
    filter_set = CategoryFilter
    template_name = "categories/category_list.html"
    order_by = ('name',)

def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render_to_response('my_app/template.html', {'filter': f})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryList, self).dispatch(*args, **kwargs)


class CategoryCRUDView(object):
    model = Category
    form_class = CategoryForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('category_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryCRUDView, self).dispatch(*args, **kwargs)


class CategoryCreate(CategoryCRUDView, CreateView):
    pass


class CategoryDetail(CategoryCRUDView, DetailView):
    pass


class CategoryUpdate(CategoryCRUDView, UpdateView):
    pass


class CategoryDelete(CategoryCRUDView, DeleteView):
    pass

