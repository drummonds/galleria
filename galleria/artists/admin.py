from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from .models import Artist


class ArtistAdmin(MarkdownModelAdmin):
    model = Artist
    search_fields = ['biography', 'price', 'info']

admin.site.register(Artist, ArtistAdmin)


