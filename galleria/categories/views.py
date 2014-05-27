from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from categories.forms import CategoryForm
from categories.models import Category


class CategoryCRUDView(object):
    model = Category
    form_class = CategoryForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('category_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryCRUDView, self).dispatch(*args, **kwargs)


class CategoryList(CategoryCRUDView, ListView):
    pass


class CategoryCreate(CategoryCRUDView, CreateView):
    pass


class CategoryDetail(CategoryCRUDView, DetailView):
    pass


class CategoryUpdate(CategoryCRUDView, UpdateView):
    pass


class CategoryDelete(CategoryCRUDView, DeleteView):
    pass

