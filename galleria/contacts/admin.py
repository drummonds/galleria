from django.contrib import admin
from .models import ContactType, Contact, PhoneNumber, Address, Note

class ContactTypeAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'name')
	list_editable = ('name',)

class NoteInline(admin.TabularInline):
	model = Note

class AddressInline(admin.StackedInline):
	model = Address

class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber

class ContactAdmin(admin.ModelAdmin):
	inlines = [NoteInline, AddressInline, PhoneNumberInline]

admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Contact, ContactAdmin)
