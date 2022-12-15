from django.contrib import admin
from .models import Person


class ListingPerson(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 2
    ordering = ['name']


admin.site.register(Person, ListingPerson)
# admin.site.register(Recipe)
