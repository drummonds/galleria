# coding: utf-8
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import Category


class CategoryTable(tables.Table):
    name = tables.LinkColumn('category_detail', args=[A('pk')])
    summary = tables.Column(order_by=("name"))

    class Meta:
        model = Category
        exclude = ('description',)

    buttons = tables.TemplateColumn(template_name='categories/category_buttons.html',orderable=False)


class ThemedCategoryTable(CategoryTable):
    class Meta:
        attrs = {'class': 'paleblue'}
