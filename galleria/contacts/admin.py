from django.contrib import admin
from contacts.models import ContactType

admin.site.register(ContactType, admin.ModelAdmin)
