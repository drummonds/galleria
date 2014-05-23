from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from extra_views import UpdateWithInlinesView, InlineFormSet

from .models import Contact, PhoneNumber, Address, Note

class PhoneNumberInline(InlineFormSet):
	model = PhoneNumber

class AddressInline(InlineFormSet):
	model = Address

class NoteInline(InlineFormSet):
	model = Note

class ContactUpdate(UpdateWithInlinesView):
	model = Contact
	inlines = [NoteInline, AddressInline, PhoneNumberInline]


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

