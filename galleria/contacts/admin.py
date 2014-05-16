from django.contrib import admin
from contacts.models import ContactType

class ContactTypeAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'name')
	list_editable = ('name',)

admin.site.register(ContactType, ContactTypeAdmin)
