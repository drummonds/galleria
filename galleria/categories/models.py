from django.core.urlresolvers import reverse
from django.db import models

import django_tables2 as tables
import django_filters

class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True,default='')

    def __str__(self):
        return("{}".format(self.name))

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

    @property
    def summary(self):
        if self.description:
            return("{} (Descr: {}...)".format(self.name, self.description[:30]))
        else:
            return("{} (No descr yet)".format(self.name))

    class Meta:
        verbose_name_plural = 'categories'


class CategoryTable(tables.Table):
    class Meta:
        model = Category

class CategoryList(tables.SingleTableView):
    model=Category
    table_class = CategoryTable


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='contains')
    description = django_filters.CharFilter(lookup_type='contains')
    class Meta:
        model = Category
        fields = ['name', 'description']



