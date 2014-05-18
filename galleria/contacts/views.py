from extra_views import UpdateWithInlinesView, InlineFormSet

from models import Contact, PhoneNumber, Address, Note

class PhoneNumberInline(InlineFormSet):
	model = PhoneNumber

class AddressInline(InlineFormSet):
	model = Address

class NoteInline(InlineFormSet):
	model = Note

class ContactUpdate(UpdateWithInlinesView):
	model = Contact
	inlines = [NoteInline, AddressInline, PhoneNumberInline]