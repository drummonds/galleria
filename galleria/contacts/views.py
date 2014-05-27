from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from extra_views import UpdateWithInlinesView, InlineFormSet

from .forms import ContactForm,ContactTypeForm
from .models import Contact, PhoneNumber, Address, Note, ContactType


class PhoneNumberInline(InlineFormSet):
    model = PhoneNumber

class AddressInline(InlineFormSet):
    model = Address

class NoteInline(InlineFormSet):
    model = Note

class ContactUpdate(UpdateWithInlinesView):
    model = Contact
    inlines = [NoteInline, AddressInline, PhoneNumberInline]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactUpdate, self).dispatch(*args, **kwargs)


class ContactView(TemplateView):
    template_name = 'contacts.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactView, self).dispatch(*args, **kwargs)


class ContactTypeView(TemplateView):
    template_name = 'contacttypess.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactTypeView, self).dispatch(*args, **kwargs)

class ContactCRUDView(object):
    model = Contact
    form_class = ContactForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('contact_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactCRUDView, self).dispatch(*args, **kwargs)


class ContactList(ContactCRUDView, ListView):
    pass


class ContactCreate(ContactCRUDView, CreateView):
    pass


class ContactDetail(ContactCRUDView, DetailView):
    pass


class ContactUpdate(ContactCRUDView, UpdateView):
    pass


class ContactDelete(ContactCRUDView, DeleteView):
    pass

class ContactTypeCRUDView(object):
    model = ContactType
    form_class = ContactTypeForm
    paginate_by = 20

    def get_success_url(self):
        return reverse('contacttype_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactTypeCRUDView, self).dispatch(*args, **kwargs)


class ContactTypeList(ContactTypeCRUDView, ListView):
    pass


class ContactTypeCreate(ContactTypeCRUDView, CreateView):
    pass


class ContactTypeDetail(ContactTypeCRUDView, DetailView):
    pass


class ContactTypeUpdate(ContactTypeCRUDView, UpdateView):
    pass


class ContactTypeDelete(ContactTypeCRUDView, DeleteView):
    pass

