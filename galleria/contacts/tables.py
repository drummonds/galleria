# coding: utf-8
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import Contact


class ContactTable(tables.Table):
    name_first = tables.LinkColumn('category_detail', args=[A('pk')])
    name_last = tables.Column(order_by=("name"))

    class Meta:
        model = Contact
        include = ('type','name_first','name_last',)
        exclude = ('id','created','modified','suffix','client_is','addressed_as','addressed_as_custom','is_company','migration_id',)

    buttons = tables.TemplateColumn(template_name='contacts/category_buttons.html',orderable=False)


class ThemedContactTable(ContactTable):
    class Meta:
        attrs = {'class': 'paleblue'}
