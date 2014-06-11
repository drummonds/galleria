from django.contrib import admin
from .models import ContactType, Contact, PhoneNumber, Address, Note

class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name')
    list_editable = ('name',)

class NoteInline(admin.TabularInline):
    model = Note

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(NoteInline, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'note':
            field.widget.attrs['class'] = 'h3noteclass ' + field.widget.attrs.get('class', '')
            field.widget.attrs['width'] = '800px'
        return field

class AddressInline(admin.StackedInline):
    model = Address

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber

class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name_first', 'name_last')
    inlines = [NoteInline, AddressInline, PhoneNumberInline]
    search_fields = ['name_first', 'name_last']
    filter_horizontal = ('categories',)

    class Media:
        css = {
             'all': ('contacts/notes.css',) # appended to static root
        }


admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(Contact, ContactAdmin)

